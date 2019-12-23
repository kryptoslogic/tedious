import lxml.etree as ET

"""
Unlike the contents of the maltego submodule, this module has been written
by a real human!
"""

entity_map = {} # every imported entity class adds itself to this dict (not actually used for anything yet...)


def stringify_value(value, value_type): # TODO make robust
	return str(value).encode()


def parse_value(value_string, value_type): # TODO make robust
	return value_string


class MaltegoEntity():
	"""
	Base class that represents a Maltego Entity.
	All other entities inherit from this.
	
	Provides methods for encoding and decoding from `<Entity>` XML Objects.
	"""
	
	id = None
	displayName = None
	displayNamePlural = None
	value = None
	
	weight = None
	display_information = {}
	additional_fields = {}
	icon_url = None
	
	_fields = {}
	
	def __init__(self, value, **kwargs):
		self.value = str(value)
		self.weight = kwargs.get("weight")
		self.display_information = kwargs.get("display_information", {})
		self.additional_fields = kwargs.get("additional_fields", {})
		self.icon_url = kwargs.get("icon_url")
	
	@classmethod
	def _get_fields(cls):
		"""
		Merge _fields metadata from parent classes
		"""
		fields = {}
		for parent_class in cls.__mro__:
			if issubclass(parent_class, MaltegoEntity):
				fields.update(parent_class._fields)
		return fields
	
	def to_xml(self):
		entity = ET.Element("Entity", Type=self.id)
		
		value = ET.Element("Value")
		value.text = str(self.value)
		entity.append(value)
		
		if self.weight is not None:
			weight = ET.Element("Weight")
			weight.text = str(self.weight)
			entity.append(weight)
		
		fields = ET.Element("AdditionalFields")
		for pyname, properties in self._get_fields().items():
			field_value = getattr(self, pyname, None)
			if field_value is not None:
				field = ET.Element("Field", Name=properties["name"])
				field.text = stringify_value(field_value, properties["type"])
				fields.append(field)
		
		if self.additional_fields:
			for field_name, field_value in self.additional_fields.items():
				field = ET.Element("Field", Name=field_name, DisplayName=field_name)
				field.text = field_value
				fields.append(field)
		
		entity.append(fields)
		
		if self.display_information:
			di = ET.Element("DisplayInformation")
			for label_name, label_html in self.display_information.items():
				label = ET.Element("Label", Name=label_name, Type="text/html")
				label.text = label_html
				di.append(label)
			entity.append(di)
		
		if self.icon_url is not None:
			iconurl = ET.Element("IconURL")
			iconurl.text = self.icon_url
			entity.append(iconurl)
		
		return entity
	
	@classmethod
	def from_xml(cls, entity_xml):
		entity_type = entity_xml.attrib["Type"]
		#assert(self.id.endswith(entity_type))
		value = entity_xml.find("Value").text
		params = {}
		for pyname, properties in cls._get_fields().items(): # this implementation is not optimal
			prop_value = [e.text for e in entity_xml.findall("AdditionalFields/Field") if e.attrib["Name"] == properties["name"]]
			if prop_value:
				params[pyname] = parse_value(prop_value[0], properties["type"])
		return cls(value, **params)


	@classmethod
	def to_entity_xml(cls):
		me = ET.Element("MaltegoEntity")
		me.attrib["id"] = cls.id
		me.attrib["displayName"] = cls.displayName
		me.attrib["displayNamePlural"] = cls.displayNamePlural
		me.attrib["description"] = cls.__doc__.strip()
		
		parent_id = cls.__mro__[1].id
		if parent_id is not None:
			bes = ET.Element("BaseEntities")
			be = ET.Element("BaseEntity")
			be.text = parent_id
			bes.append(be)
			me.append(bes)
		
		props = ET.Element("Properties")
		fields = ET.Element("Fields")
		
		for pyname, properties in cls._fields.items():
			field = ET.Element("Field")
			field.attrib["name"] = properties["name"]
			field.attrib["displayName"] = properties["name"]
			field.attrib["type"] = "string"
			field.attrib["nullable"] = "true"
			fields.append(field)
		
		props.append(fields)
		me.append(props)
		
		return me
