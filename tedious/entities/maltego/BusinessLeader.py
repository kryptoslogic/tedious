# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="People" conversionOrder="2147483647" description="A very wealthy or powerful businessman such as a CEO" displayName="Business Leader" displayNamePlural="Business Leaders" id="maltego.BusinessLeader" largeIconResource="CEO" smallIconResource="CEO" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.Businessman</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="">
	      <Fields />
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.Businessman import Businessman

class BusinessLeader(Businessman):
	"""
	A very wealthy or powerful businessman such as a CEO
	"""

	id = 'maltego.BusinessLeader'
	displayName = 'Business Leader'
	displayNamePlural = 'Business Leaders'


	_fields = {
	}

	def __init__(self, value, **kwargs):
		super().__init__(value, **kwargs)

entities.entity_map[BusinessLeader.id] = BusinessLeader
