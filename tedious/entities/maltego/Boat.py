# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Transportation" conversionOrder="2147483647" description="A vessel propelled on water by oars, sails, or an engine" displayName="Boat / Ship" displayNamePlural="Boats / Ships" id="maltego.Boat" largeIconResource="Ship" smallIconResource="Ship" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.Transport</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="">
	      <Fields>
	         <Field description="Make of the bike / bicycle" displayName="Make" hidden="false" name="transport.make" nullable="true" readonly="false" type="string">
	            <SampleValue>Ferry</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.Transport import Transport

class Boat(Transport):
	"""
	A vessel propelled on water by oars, sails, or an engine
	"""

	id = 'maltego.Boat'
	displayName = 'Boat / Ship'
	displayNamePlural = 'Boats / Ships'

	transport_make = None # string transport.make

	_fields = {
		'transport_make': {'name': 'transport.make', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, transport_make=None, **kwargs):
		super().__init__(value, **kwargs)
		self.transport_make = transport_make

entities.entity_map[Boat.id] = Boat
