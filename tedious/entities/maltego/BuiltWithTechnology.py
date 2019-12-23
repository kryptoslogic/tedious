# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Penetration Testing" conversionOrder="2147483647" description="A Technology identified by BuiltWith" displayName="BuiltWith Technology" displayNamePlural="BuiltWith Technologies" id="maltego.BuiltWithTechnology" largeIconResource="BuiltWith" smallIconResource="BuiltWith" visible="true">
	   <Properties displayValue="builtwith.technology" value="builtwith.technology">
	      <Fields>
	         <Field description="" displayName="BuiltWith Technology" hidden="false" name="builtwith.technology" nullable="true" readonly="false" type="string">
	            <SampleValue>BuiltWith Technology</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities

class BuiltWithTechnology(entities.MaltegoEntity):
	"""
	A Technology identified by BuiltWith
	"""

	id = 'maltego.BuiltWithTechnology'
	displayName = 'BuiltWith Technology'
	displayNamePlural = 'BuiltWith Technologies'

	builtwith_technology = None # string builtwith.technology

	_fields = {
		'builtwith_technology': {'name': 'builtwith.technology', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, builtwith_technology=None, **kwargs):
		super().__init__(value, **kwargs)
		self.builtwith_technology = builtwith_technology

entities.entity_map[BuiltWithTechnology.id] = BuiltWithTechnology
