# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="false" category="People" conversionOrder="2147483647" description="A person who is on your side" displayName="Good Guy" displayNamePlural="Good Guys" id="maltego.GoodGuy" largeIconResource="Person" smallIconResource="Person" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.Person</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="">
	      <Fields />
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.Person import Person

class GoodGuy(Person):
	"""
	A person who is on your side
	"""

	id = 'maltego.GoodGuy'
	displayName = 'Good Guy'
	displayNamePlural = 'Good Guys'


	_fields = {
	}

	def __init__(self, value, **kwargs):
		super().__init__(value, **kwargs)

entities.entity_map[GoodGuy.id] = GoodGuy
