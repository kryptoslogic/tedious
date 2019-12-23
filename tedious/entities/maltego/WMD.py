# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="false" category="Weapons" conversionOrder="2147483647" description="A weapon capable of causing widespread death and destruction" displayName="Weapon of Mass Destruction" displayNamePlural="Weapons of Mass Destruction" id="maltego.WMD" largeIconResource="Destroy" smallIconResource="Destroy" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.Weapon</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="weapon.type" value="weapon.type">
	      <Fields>
	         <Field description="Weapon type" displayName="Type" hidden="false" name="weapon.type" nullable="true" readonly="false" type="string">
	            <SampleValue>WMD</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.Weapon import Weapon

class WMD(Weapon):
	"""
	A weapon capable of causing widespread death and destruction
	"""

	id = 'maltego.WMD'
	displayName = 'Weapon of Mass Destruction'
	displayNamePlural = 'Weapons of Mass Destruction'

	weapon_type = None # string weapon.type

	_fields = {
		'weapon_type': {'name': 'weapon.type', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, weapon_type=None, **kwargs):
		super().__init__(value, **kwargs)
		self.weapon_type = weapon_type

entities.entity_map[WMD.id] = WMD
