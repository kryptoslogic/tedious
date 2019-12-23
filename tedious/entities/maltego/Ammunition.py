# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Weapons" conversionOrder="2147483647" description="Projectiles fired from weapons" displayName="Ammunition" displayNamePlural="Ammunition" id="maltego.Ammunition" largeIconResource="Ammunition" smallIconResource="Ammunition" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.Weapon</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="weapon.type" value="weapon.type">
	      <Fields>
	         <Field description="Weapon type" displayName="Type" hidden="false" name="weapon.type" nullable="true" readonly="false" type="string">
	            <SampleValue>Shotgun shells</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.Weapon import Weapon

class Ammunition(Weapon):
	"""
	Projectiles fired from weapons
	"""

	id = 'maltego.Ammunition'
	displayName = 'Ammunition'
	displayNamePlural = 'Ammunition'

	weapon_type = None # string weapon.type

	_fields = {
		'weapon_type': {'name': 'weapon.type', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, weapon_type=None, **kwargs):
		super().__init__(value, **kwargs)
		self.weapon_type = weapon_type

entities.entity_map[Ammunition.id] = Ammunition
