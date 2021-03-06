# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="People" conversionOrder="2147483647" description="A person who uses terrorism in the pursuit of political or other aims" displayName="Terrorist" displayNamePlural="Terrorists" id="maltego.Terrorist" largeIconResource="TerroristMember" smallIconResource="TerroristMember" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.BadGuy</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="">
	      <Fields />
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.BadGuy import BadGuy

class Terrorist(BadGuy):
	"""
	A person who uses terrorism in the pursuit of political or other aims
	"""

	id = 'maltego.Terrorist'
	displayName = 'Terrorist'
	displayNamePlural = 'Terrorists'


	_fields = {
	}

	def __init__(self, value, **kwargs):
		super().__init__(value, **kwargs)

entities.entity_map[Terrorist.id] = Terrorist
