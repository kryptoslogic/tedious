# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Personal" conversionOrder="2147483647" description="A phone number for a place of work" displayName="Phone Number (Office)" displayNamePlural="Phone Numbers (Office)" id="maltego.PhoneNumberOffice" largeIconResource="LandlinePhoneOffice" smallIconResource="LandlinePhoneOffice" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.PhoneNumber</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="">
	      <Fields />
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.PhoneNumber import PhoneNumber

class PhoneNumberOffice(PhoneNumber):
	"""
	A phone number for a place of work
	"""

	id = 'maltego.PhoneNumberOffice'
	displayName = 'Phone Number (Office)'
	displayNamePlural = 'Phone Numbers (Office)'


	_fields = {
	}

	def __init__(self, value, **kwargs):
		super().__init__(value, **kwargs)

entities.entity_map[PhoneNumberOffice.id] = PhoneNumberOffice
