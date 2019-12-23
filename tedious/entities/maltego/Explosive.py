# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Weapons" conversionOrder="2147483647" description="A substance, or a device containing a substance, that holds a great amount of potential energy that can produce an explosion if released suddenly" displayName="Explosive" displayNamePlural="Explosives" id="maltego.Explosive" largeIconResource="BombGolden" smallIconResource="BombGolden" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.Weapon</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="weapon.type" value="weapon.type">
	      <Fields>
	         <Field description="Weapon type" displayName="Type" hidden="false" name="weapon.type" nullable="true" readonly="false" type="string">
	            <SampleValue>C4</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.Weapon import Weapon

class Explosive(Weapon):
	"""
	A substance, or a device containing a substance, that holds a great amount of potential energy that can produce an explosion if released suddenly
	"""

	id = 'maltego.Explosive'
	displayName = 'Explosive'
	displayNamePlural = 'Explosives'

	weapon_type = None # string weapon.type

	_fields = {
		'weapon_type': {'name': 'weapon.type', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, weapon_type=None, **kwargs):
		super().__init__(value, **kwargs)
		self.weapon_type = weapon_type

entities.entity_map[Explosive.id] = Explosive
