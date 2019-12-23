# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Weapons" conversionOrder="2147483647" description="A device that uses biological agents to inflict death or harm to human beings" displayName="Bio Weapon" displayNamePlural="Bio Weapons" id="maltego.BioWeapon" largeIconResource="BioAgent" smallIconResource="BioAgent" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.WMD</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="weapon.type" value="weapon.type">
	      <Fields>
	         <Field description="Weapon type" displayName="Type" hidden="false" name="weapon.type" nullable="true" readonly="false" type="string">
	            <SampleValue>Anthrax</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.WMD import WMD

class BioWeapon(WMD):
	"""
	A device that uses biological agents to inflict death or harm to human beings
	"""

	id = 'maltego.BioWeapon'
	displayName = 'Bio Weapon'
	displayNamePlural = 'Bio Weapons'

	weapon_type = None # string weapon.type

	_fields = {
		'weapon_type': {'name': 'weapon.type', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, weapon_type=None, **kwargs):
		super().__init__(value, **kwargs)
		self.weapon_type = weapon_type

entities.entity_map[BioWeapon.id] = BioWeapon
