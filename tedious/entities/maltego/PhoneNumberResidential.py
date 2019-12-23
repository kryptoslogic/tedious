# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Personal" conversionOrder="2147483647" description="A phone number for a place of residence" displayName="Phone Number (Residential)" displayNamePlural="Phone Numbers (Residential)" id="maltego.PhoneNumberResidential" largeIconResource="LandlinePhoneResidential" smallIconResource="LandlinePhoneResidential" visible="true">
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

class PhoneNumberResidential(PhoneNumber):
	"""
	A phone number for a place of residence
	"""

	id = 'maltego.PhoneNumberResidential'
	displayName = 'Phone Number (Residential)'
	displayNamePlural = 'Phone Numbers (Residential)'


	_fields = {
	}

	def __init__(self, value, **kwargs):
		super().__init__(value, **kwargs)

entities.entity_map[PhoneNumberResidential.id] = PhoneNumberResidential