# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Locations" conversionOrder="2147483647" description="A sheltered port where ships can load or unload passengers or goods" displayName="Harbor" displayNamePlural="Harbors" id="maltego.Harbor" largeIconResource="Ship" smallIconResource="Ship" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.TransportHub</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="">
	      <Fields>
	         <Field description="" displayName="Name" hidden="false" name="location.name" nullable="true" readonly="false" type="string">
	            <SampleValue>Port of Cape Town</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.TransportHub import TransportHub

class Harbor(TransportHub):
	"""
	A sheltered port where ships can load or unload passengers or goods
	"""

	id = 'maltego.Harbor'
	displayName = 'Harbor'
	displayNamePlural = 'Harbors'

	location_name = None # string location.name

	_fields = {
		'location_name': {'name': 'location.name', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, location_name=None, **kwargs):
		super().__init__(value, **kwargs)
		self.location_name = location_name

entities.entity_map[Harbor.id] = Harbor
