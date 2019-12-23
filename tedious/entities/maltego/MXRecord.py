# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Infrastructure" conversionOrder="2147483647" description="A DNS mail exchange record" displayName="MX Record" displayNamePlural="MX Records" id="maltego.MXRecord" largeIconResource="MX Record" smallIconResource="MX Record" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.DNSName</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="fqdn" value="fqdn">
	      <Fields>
	         <Field description="" displayName="MX Record" hidden="false" name="fqdn" nullable="true" readonly="false" type="string">
	            <SampleValue>mail.paterva.com</SampleValue>
	         </Field>
	         <Field description="" displayName="Priority" hidden="false" name="mxrecord.priority" nullable="true" readonly="false" type="int">
	            <SampleValue>0</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.DNSName import DNSName

class MXRecord(DNSName):
	"""
	A DNS mail exchange record
	"""

	id = 'maltego.MXRecord'
	displayName = 'MX Record'
	displayNamePlural = 'MX Records'

	fqdn = None # string fqdn
	mxrecord_priority = None # int mxrecord.priority

	_fields = {
		'fqdn': {'name': 'fqdn', 'type': 'string', 'nullable': 'true'},
		'mxrecord_priority': {'name': 'mxrecord.priority', 'type': 'int', 'nullable': 'true'},
	}

	def __init__(self, value, fqdn=None, mxrecord_priority=None, **kwargs):
		super().__init__(value, **kwargs)
		self.fqdn = fqdn
		self.mxrecord_priority = mxrecord_priority

entities.entity_map[MXRecord.id] = MXRecord
