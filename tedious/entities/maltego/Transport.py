# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="false" category="Transportation" conversionOrder="2147483647" description="A device that is used to transport people or cargo" displayName="Transport" displayNamePlural="Transports" id="maltego.Transport" largeIconResource="Car" smallIconResource="Car" visible="true">
	   <Properties displayValue="transport.name" value="transport.name">
	      <Fields>
	         <Field description="Name of the airplane" displayName="Name" evaluator="maltego.replace" hidden="false" name="transport.name" nullable="true" readonly="false" type="string">
	            <DefaultValue>$trim($property(transport.make) $property(transport.model))</DefaultValue>
	            <SampleValue />
	         </Field>
	         <Field description="Make of the transport" displayName="Make" hidden="false" name="transport.make" nullable="true" readonly="false" type="string">
	            <SampleValue>TIE fighter</SampleValue>
	         </Field>
	         <Field description="Model of the transport" displayName="Model" hidden="false" name="transport.model" nullable="true" readonly="false" type="string">
	            <SampleValue />
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities

class Transport(entities.MaltegoEntity):
	"""
	A device that is used to transport people or cargo
	"""

	id = 'maltego.Transport'
	displayName = 'Transport'
	displayNamePlural = 'Transports'

	transport_name = None # string transport.name
	transport_make = None # string transport.make
	transport_model = None # string transport.model

	_fields = {
		'transport_name': {'name': 'transport.name', 'type': 'string', 'nullable': 'true'},
		'transport_make': {'name': 'transport.make', 'type': 'string', 'nullable': 'true'},
		'transport_model': {'name': 'transport.model', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, transport_name=None, transport_make=None, transport_model=None, **kwargs):
		super().__init__(value, **kwargs)
		self.transport_name = transport_name
		self.transport_make = transport_make
		self.transport_model = transport_model

entities.entity_map[Transport.id] = Transport