# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="People" conversionOrder="2147483647" description="An unknown person thought to be guilty of a crime or offense" displayName="Unknown Suspect" displayNamePlural="Unknown Suspects" id="maltego.Unsub" largeIconResource="UnknownSuspect" smallIconResource="UnknownSuspect" visible="true">
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

class Unsub(BadGuy):
	"""
	An unknown person thought to be guilty of a crime or offense
	"""

	id = 'maltego.Unsub'
	displayName = 'Unknown Suspect'
	displayNamePlural = 'Unknown Suspects'


	_fields = {
	}

	def __init__(self, value, **kwargs):
		super().__init__(value, **kwargs)

entities.entity_map[Unsub.id] = Unsub
