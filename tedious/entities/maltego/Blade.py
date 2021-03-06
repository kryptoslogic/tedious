# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Weapons" conversionOrder="2147483647" description="A sharp edged weapon such as a knife" displayName="Blade" displayNamePlural="Blades" id="maltego.Blade" largeIconResource="Knife" smallIconResource="Knife" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.Weapon</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="weapon.type" value="weapon.type">
	      <Fields>
	         <Field description="Weapon type" displayName="Type" hidden="false" name="weapon.type" nullable="true" readonly="false" type="string">
	            <SampleValue>Knife</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.Weapon import Weapon

class Blade(Weapon):
	"""
	A sharp edged weapon such as a knife
	"""

	id = 'maltego.Blade'
	displayName = 'Blade'
	displayNamePlural = 'Blades'

	weapon_type = None # string weapon.type

	_fields = {
		'weapon_type': {'name': 'weapon.type', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, weapon_type=None, **kwargs):
		super().__init__(value, **kwargs)
		self.weapon_type = weapon_type

entities.entity_map[Blade.id] = Blade
