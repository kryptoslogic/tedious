# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Locations" conversionOrder="250" description="A circular area somewhere on Earth" displayName="Circular Area" displayNamePlural="Circular Areas" id="maltego.CircularArea" largeIconResource="Circular Area" smallIconResource="Circular Area" visible="true">
	   <Converter>
	      <Value>^\s*([\-\d.]+)\s*,\s*([\-\d.]+)\s*,\s*([\d]+)m?\s*$</Value>
	      <RegexGroups>
	         <RegexGroup property="latitude" />
	         <RegexGroup property="longitude" />
	         <RegexGroup property="radius" />
	      </RegexGroups>
	   </Converter>
	   <Properties displayValue="area.circular" value="area.circular">
	      <Fields>
	         <Field description="" displayName="Circular Area" evaluator="maltego.replace" hidden="false" name="area.circular" nullable="true" readonly="false" type="string">
	            <DefaultValue>$property(latitude),$property(longitude),$property(radius)m</DefaultValue>
	            <SampleValue />
	         </Field>
	         <Field description="" displayName="Latitude" hidden="false" name="latitude" nullable="true" readonly="false" type="float">
	            <SampleValue>38.951633</SampleValue>
	         </Field>
	         <Field description="" displayName="Longitude" hidden="false" name="longitude" nullable="true" readonly="false" type="float">
	            <SampleValue>-77.14462</SampleValue>
	         </Field>
	         <Field description="" displayName="Radius (m)" hidden="false" name="radius" nullable="true" readonly="false" type="int">
	            <SampleValue>1000</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	   <Actions>
	      <Action displayName="Google Maps Me!" name="maltego.spec.action.googlemaps" type="maltego.spec.action.type.browser">
	         <Config>http://maps.google.com/maps?ll=$property(latitude),$property(longitude)</Config>
	      </Action>
	   </Actions>
	</MaltegoEntity>

"""

import tedious.entities as entities

class CircularArea(entities.MaltegoEntity):
	"""
	A circular area somewhere on Earth
	"""

	id = 'maltego.CircularArea'
	displayName = 'Circular Area'
	displayNamePlural = 'Circular Areas'

	area_circular = None # string area.circular
	latitude = None # float latitude
	longitude = None # float longitude
	radius = None # int radius

	_fields = {
		'area_circular': {'name': 'area.circular', 'type': 'string', 'nullable': 'true'},
		'latitude': {'name': 'latitude', 'type': 'float', 'nullable': 'true'},
		'longitude': {'name': 'longitude', 'type': 'float', 'nullable': 'true'},
		'radius': {'name': 'radius', 'type': 'int', 'nullable': 'true'},
	}

	def __init__(self, value, area_circular=None, latitude=None, longitude=None, radius=None, **kwargs):
		super().__init__(value, **kwargs)
		self.area_circular = area_circular
		self.latitude = latitude
		self.longitude = longitude
		self.radius = radius

entities.entity_map[CircularArea.id] = CircularArea
