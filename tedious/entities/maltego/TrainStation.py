# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Locations" conversionOrder="2147483647" description="A terminal where trains load or unload passengers or goods" displayName="Train Station" displayNamePlural="Train Stations" id="maltego.TrainStation" largeIconResource="TrainStation" smallIconResource="TrainStation" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.TransportHub</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="">
	      <Fields>
	         <Field description="" displayName="Name" hidden="false" name="location.name" nullable="true" readonly="false" type="string">
	            <SampleValue>Grand Central</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.TransportHub import TransportHub

class TrainStation(TransportHub):
	"""
	A terminal where trains load or unload passengers or goods
	"""

	id = 'maltego.TrainStation'
	displayName = 'Train Station'
	displayNamePlural = 'Train Stations'

	location_name = None # string location.name

	_fields = {
		'location_name': {'name': 'location.name', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, location_name=None, **kwargs):
		super().__init__(value, **kwargs)
		self.location_name = location_name

entities.entity_map[TrainStation.id] = TrainStation