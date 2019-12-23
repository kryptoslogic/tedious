# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Devices" conversionOrder="2147483647" description="A device which can make and receive telephone calls over a radio link whilst moving around a wide geographic area" displayName="Mobile Phone" displayNamePlural="Mobile Phones" id="maltego.MobilePhone" largeIconResource="MobilePhoneGolden" smallIconResource="MobilePhoneGolden" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.Device</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="device" value="device">
	      <Fields>
	         <Field description="device" displayName="Device" hidden="false" name="device" nullable="true" readonly="false" type="string">
	            <SampleValue>Nokia</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.Device import Device

class MobilePhone(Device):
	"""
	A device which can make and receive telephone calls over a radio link whilst moving around a wide geographic area
	"""

	id = 'maltego.MobilePhone'
	displayName = 'Mobile Phone'
	displayNamePlural = 'Mobile Phones'

	device = None # string device

	_fields = {
		'device': {'name': 'device', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, device=None, **kwargs):
		super().__init__(value, **kwargs)
		self.device = device

entities.entity_map[MobilePhone.id] = MobilePhone
