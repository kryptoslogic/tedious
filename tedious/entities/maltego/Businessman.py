# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="People" conversionOrder="2147483647" description="A person involved in activities for the purpose of generating revenue" displayName="Businessman / Employee" displayNamePlural="Businessmen / Employees" id="maltego.Businessman" largeIconResource="Businessman" smallIconResource="Businessman" visible="true">
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

class Businessman(Person):
	"""
	A person involved in activities for the purpose of generating revenue
	"""

	id = 'maltego.Businessman'
	displayName = 'Businessman / Employee'
	displayNamePlural = 'Businessmen / Employees'


	_fields = {
	}

	def __init__(self, value, **kwargs):
		super().__init__(value, **kwargs)

entities.entity_map[Businessman.id] = Businessman
