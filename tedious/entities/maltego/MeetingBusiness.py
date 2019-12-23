# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Events" conversionOrder="2147483647" description="A gathering of people for a commercial purpose" displayName="Meeting (Business)" displayNamePlural="Meetings (Business)" id="maltego.MeetingBusiness" largeIconResource="MeetingBusiness" smallIconResource="MeetingBusiness" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.Meeting</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="">
	      <Fields />
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.Meeting import Meeting

class MeetingBusiness(Meeting):
	"""
	A gathering of people for a commercial purpose
	"""

	id = 'maltego.MeetingBusiness'
	displayName = 'Meeting (Business)'
	displayNamePlural = 'Meetings (Business)'


	_fields = {
	}

	def __init__(self, value, **kwargs):
		super().__init__(value, **kwargs)

entities.entity_map[MeetingBusiness.id] = MeetingBusiness
