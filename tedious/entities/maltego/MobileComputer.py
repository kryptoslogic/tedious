# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Devices" conversionOrder="2147483647" description="A portable computer suitable for use while traveling" displayName="Mobile Computer" displayNamePlural="Mobile Computers" id="maltego.MobileComputer" largeIconResource="MobileComputer" smallIconResource="MobileComputer" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.Computer</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="device" value="device">
	      <Fields>
	         <Field description="device" displayName="Device" hidden="false" name="device" nullable="true" readonly="false" type="string">
	            <SampleValue>MacBook</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.Computer import Computer

class MobileComputer(Computer):
	"""
	A portable computer suitable for use while traveling
	"""

	id = 'maltego.MobileComputer'
	displayName = 'Mobile Computer'
	displayNamePlural = 'Mobile Computers'

	device = None # string device

	_fields = {
		'device': {'name': 'device', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, device=None, **kwargs):
		super().__init__(value, **kwargs)
		self.device = device

entities.entity_map[MobileComputer.id] = MobileComputer
