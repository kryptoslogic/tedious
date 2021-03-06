# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Malware" conversionOrder="2147483647" description="Authentihash" displayName="Authentihash" displayNamePlural="Authentihashs" id="maltego.Authentihash" largeIconResource="Bit" smallIconResource="Bit" visible="true">
	   <Properties displayValue="properties.authentihash" value="properties.authentihash">
	      <Fields>
	         <Field description="" displayName="Authentihash" hidden="false" name="properties.authentihash" nullable="true" readonly="false" type="string">
	            <DefaultValue> </DefaultValue>
	            <SampleValue>-</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities

class Authentihash(entities.MaltegoEntity):
	"""
	Authentihash
	"""

	id = 'maltego.Authentihash'
	displayName = 'Authentihash'
	displayNamePlural = 'Authentihashs'

	properties_authentihash = None # string properties.authentihash

	_fields = {
		'properties_authentihash': {'name': 'properties.authentihash', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, properties_authentihash=None, **kwargs):
		super().__init__(value, **kwargs)
		self.properties_authentihash = properties_authentihash

entities.entity_map[Authentihash.id] = Authentihash
