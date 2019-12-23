# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Transportation" conversionOrder="2147483647" description="A powered flying vehicle with fixed wings" displayName="Plane" displayNamePlural="Planes" id="maltego.Plane" largeIconResource="Plane" smallIconResource="Plane" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.Transport</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="">
	      <Fields>
	         <Field description="Make of the airplane" displayName="Make" hidden="false" name="transport.make" nullable="true" readonly="false" type="string">
	            <SampleValue>Airbus</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.Transport import Transport

class Plane(Transport):
	"""
	A powered flying vehicle with fixed wings
	"""

	id = 'maltego.Plane'
	displayName = 'Plane'
	displayNamePlural = 'Planes'

	transport_make = None # string transport.make

	_fields = {
		'transport_make': {'name': 'transport.make', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, transport_make=None, **kwargs):
		super().__init__(value, **kwargs)
		self.transport_make = transport_make

entities.entity_map[Plane.id] = Plane
