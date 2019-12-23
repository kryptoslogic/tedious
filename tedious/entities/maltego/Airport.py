# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Locations" conversionOrder="2147483647" description="A complex of runways and buildings for the takeoff, landing, and maintenance of aircraft" displayName="Airport" displayNamePlural="Airports" id="maltego.Airport" largeIconResource="Airport" smallIconResource="Airport" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.TransportHub</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="">
	      <Fields>
	         <Field description="" displayName="Name" hidden="false" name="location.name" nullable="true" readonly="false" type="string">
	            <SampleValue>O.R. Tambo</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.TransportHub import TransportHub

class Airport(TransportHub):
	"""
	A complex of runways and buildings for the takeoff, landing, and maintenance of aircraft
	"""

	id = 'maltego.Airport'
	displayName = 'Airport'
	displayNamePlural = 'Airports'

	location_name = None # string location.name

	_fields = {
		'location_name': {'name': 'location.name', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, location_name=None, **kwargs):
		super().__init__(value, **kwargs)
		self.location_name = location_name

entities.entity_map[Airport.id] = Airport