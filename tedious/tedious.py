from flask import Flask, request, Response
from collections import namedtuple
import lxml.etree as ET
from enum import Enum
import traceback
import sys
import hashlib

import tedious.entities as entities
import tedious.entities.maltego as maltego


# TODO: make this a class
Transform = namedtuple("Transform", ["handler", "ein", "eout", "dispname"])


class UIMessageType(Enum):
	FATAL_ERROR = "FatalError" # Shows in a pop-up message box
	PARTIAL_ERROR = "PartialError" # shows in the Transform Output panel with an Orange font
	INFORM = "Inform" # shows in the Transform Output panel
	DEBUG = "Debug" # shows in the Transform Output panel in a grey font, only if the display filter is adjusted 


class UIMessage():
	def __init__(self, message, message_type=UIMessageType.INFORM):
		self.message = message
		self.message_type = message_type
	
	def to_xml(self):
		uimessage = ET.Element("UIMessage", MessageType=self.message_type.value)
		uimessage.text = self.message
		return uimessage


class Tedious(Flask):
	def __init__(self, import_name, *args, **kwargs):
		super().__init__(import_name, *args, **kwargs)
		self.transforms = {}
		self.add_url_rule("/", view_func=self.hello)
		self.add_url_rule("/seed", view_func=self.seed)
		self.add_url_rule("/runner", view_func=self.runner, methods=["GET", "POST"])
	
	def hello(self):
		return "This is a Tedious Transform server - please use /seed to seed your Maltego client."
	
	def seed(self):
		# TODO: Don't hardcode this
		output_xml = """<MaltegoMessage>
  <MaltegoTransformDiscoveryMessage source="PythonTestServer">
    <TransformApplications>
      <TransformApplication
      name="tedious Test"
      requireAPIKey="false"
      registrationURL="http://www.paterva.com/web2/NOAPIKEY.html"
      URL="https://localhost:31337/runner"></TransformApplication>
    </TransformApplications>
    <OtherSeedServers></OtherSeedServers>
  </MaltegoTransformDiscoveryMessage>
</MaltegoMessage>"""
		return Response(output_xml, mimetype="text/xml")
	
	def runner(self):
		cmd = request.args.get("Command")
		if cmd == "_TRANSFORMS":
			return self.get_transforms()
		elif cmd == "_RUN":
			return self.run_transform(request.args.get("TransformToRun"))
		elif cmd == "_CONFIG":
			# TODO: have the option to pass a real config archive
			return Response(b"", status=200, mimetype='application/octet-stream')
	
	def get_transforms(self):
		mm = ET.Element("MaltegoMessage")
		mtlm = ET.Element("MaltegoTransformListMessage")
		transforms = ET.Element("Transforms")
		
		for name, properties in self.transforms.items():
			maindoc, paramdoc = self._parse_parameter_docstring(properties.handler.__doc__)
			
			t = ET.Element("Transform")
			t.attrib["Owner"] = "Example Owner"
			t.attrib["Description"] = maindoc
			t.attrib["UIDisplayName"] = properties.dispname
			t.attrib["Author"] = "Example Author"
			t.attrib["TransformName"] = name
			
			t.attrib["Version"] = "0"
			t.attrib["MaxEntityInputCount"] = "0"
			t.attrib["MaxEntityOutputCount"] = "0"
			t.attrib["LocationRelevance"] = "global"
			
			outents = ET.Element("OutputEntities")
			outent = ET.Element("OutputEntity")
			outent.text = properties.eout.id
			outents.append(outent)
			t.append(outents)
			
			if properties.handler.__kwdefaults__:
				inreqs = ET.Element("UIInputRequirements")
				for argname, argdefault in properties.handler.__kwdefaults__.items():
					inreqs.append(ET.Element("Input",
						Name=argname,
						Type="string",
						Display=paramdoc.get(argname, argname),
						DefaultValue=str(argdefault),
						Optional="False",
						Popup="True"))
				t.append(inreqs)
			
			inent = ET.Element("InputEntity")
			inent.text = properties.ein.id
			t.append(inent)
			
			transforms.append(t)
		
		mtlm.append(transforms)
		mm.append(mtlm)
		return Response(ET.tostring(mm, pretty_print=True), mimetype="text/xml")
	
	def run_transform(self, name):
		transform = self.transforms[name]
		
		if self.debug:
			print("\n[debug] TRANSFORM REQUEST:")
			print(request.data.decode())
		
		request_xml = ET.fromstring(request.data)
		# TODO support multiple request entities
		request_entity = request_xml.find("MaltegoTransformRequestMessage/Entities/Entity")
		request_object = transform.ein.from_xml(request_entity)
		request_fields = {field.attrib["Name"]: field.text
			for field in request_xml.findall("MaltegoTransformRequestMessage/TransformFields/Field")}
		
		response = ET.Element("MaltegoMessage")
		respmsg = ET.Element("MaltegoTransformResponseMessage")
		entities = ET.Element("Entities")
		messages = ET.Element("UIMessages")
		
		try:
			# actually do the transform
			result = transform.handler(request_object, **request_fields)
			try:
				result_list = list(result)
			except TypeError:
				result_list = [result]
			
			for result in result_list:
				if isinstance(result, UIMessage):
					messages.append(result.to_xml())
				elif hasattr(result, "to_xml"):
					entities.append(result.to_xml())
				else:
					# TODO: proper logging
					print("WARNING: unable to serialise entity: {}".format(result))
		
		except Exception:
			error_text = "[Tedious] A Python exception occured while executing the transform:\n\n"
			if self.debug:
				error_text += "".join(traceback.format_exception(*sys.exc_info()))
			else:
				error_text += "Set FLASK_DEBUG=1 to enable backtraces."
			messages.append(UIMessage(error_text, UIMessageType.FATAL_ERROR).to_xml())
		
		respmsg.append(entities)
		respmsg.append(messages)
		response.append(respmsg)
		
		resp = ET.tostring(response, pretty_print=True)
		
		if self.debug:
			print("\n[debug] TRANSFORM RESPONSE:")
			print(resp.decode())
		
		return Response(resp, mimetype="text/xml")
	
	def transform(self, name, ein=maltego.Phrase, eout=maltego.Phrase):
		def decorator(handler):
			self.transforms[self._normalize_name(name)] = Transform(handler, ein, eout, name)
			return handler
		return decorator
	
	def _parse_parameter_docstring(self, docstring):
		if not docstring:
			return "", {}

		lines = [line.strip() for line in docstring.strip().split("\n")]
		if "" not in lines:
			return " ".join(lines), {}

		maindoc = " ".join(lines[:lines.index("")])
		paramdoc = {}
		for line in lines[lines.index("")+1:]:
			argname, argdoc = line.split(":")
			paramdoc[argname] = argdoc

		return maindoc, paramdoc
	
	def _normalize_name(self, name):
		# non-alphanumeric chars that are still allowed
		whitelist = "_-"
		
		# Remove non-ascii chars, replace spaces with underscores
		norm_name = name.encode("ascii", "ignore").decode().replace(" ", "_")
		
		# Remove non-alphanumeric chars
		filtered_name = "".join(filter(lambda s: s.isalnum() or s in whitelist, norm_name))
		
		# Prevent accidental name collisions
		uid = hashlib.sha256(name.encode()).hexdigest()[:8]
		
		return filtered_name + "_" + uid
