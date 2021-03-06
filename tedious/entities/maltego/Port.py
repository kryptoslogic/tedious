# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Penetration Testing" conversionOrder="2147483647" description="A TCP/UDP network port" displayName="Port" displayNamePlural="Ports" id="maltego.Port" largeIconResource="Port" smallIconResource="Port" visible="true">
	   <Properties displayValue="port.number" value="port.number">
	      <Groups />
	      <Fields>
	         <Field description="" displayName="Port number" hidden="false" name="port.number" nullable="true" readonly="false" type="int">
	            <DefaultValue>80</DefaultValue>
	            <SampleValue>0</SampleValue>
	         </Field>
	         <Field description="" displayName="Port" hidden="false" name="properties.port" nullable="true" readonly="false" type="string">
	            <DefaultValue> </DefaultValue>
	            <SampleValue>443</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities

class Port(entities.MaltegoEntity):
	"""
	A TCP/UDP network port
	"""

	id = 'maltego.Port'
	displayName = 'Port'
	displayNamePlural = 'Ports'

	port_number = None # int port.number
	properties_port = None # string properties.port

	_fields = {
		'port_number': {'name': 'port.number', 'type': 'int', 'nullable': 'true'},
		'properties_port': {'name': 'properties.port', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, port_number=None, properties_port=None, **kwargs):
		super().__init__(value, **kwargs)
		self.port_number = port_number
		self.properties_port = properties_port

entities.entity_map[Port.id] = Port
