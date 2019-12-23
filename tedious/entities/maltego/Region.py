# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Locations" conversionOrder="2147483647" description="An area having definable characteristics but not always fixed boundaries or borders" displayName="Region" displayNamePlural="Regions" id="maltego.Region" largeIconResource="Geography" smallIconResource="Geography" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.Location</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="">
	      <Fields>
	         <Field description="" displayName="Name" hidden="false" name="location.name" nullable="true" readonly="false" type="string">
	            <SampleValue>Area 51</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.Location import Location

class Region(Location):
	"""
	An area having definable characteristics but not always fixed boundaries or borders
	"""

	id = 'maltego.Region'
	displayName = 'Region'
	displayNamePlural = 'Regions'

	location_name = None # string location.name

	_fields = {
		'location_name': {'name': 'location.name', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, location_name=None, **kwargs):
		super().__init__(value, **kwargs)
		self.location_name = location_name

entities.entity_map[Region.id] = Region
