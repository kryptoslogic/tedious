# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Infrastructure" conversionOrder="90" description="An internet Uniform Resource Locator (URL)" displayName="URL" displayNamePlural="URLs" id="maltego.URL" largeIconResource="URL" smallIconResource="URL" visible="true">
	   <Converter>
	      <Value>(http[s]*://([-\w\.\:]*)[-\w\.\:/]*/[^\s\?]*(\?[^\s]*)?)</Value>
	      <RegexGroups>
	         <RegexGroup property="url" />
	         <RegexGroup property="short-title" />
	      </RegexGroups>
	   </Converter>
	   <Properties displayValue="short-title" value="url">
	      <Fields>
	         <Field description="" displayName="Short title" hidden="false" name="short-title" nullable="true" readonly="false" type="string">
	            <SampleValue>URL Title</SampleValue>
	         </Field>
	         <Field description="" displayName="URL" hidden="false" name="url" nullable="true" readonly="false" type="url" />
	         <Field description="" displayName="Title" hidden="false" name="title" nullable="true" readonly="false" type="string">
	            <SampleValue>URL Title</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities

class URL(entities.MaltegoEntity):
	"""
	An internet Uniform Resource Locator (URL)
	"""

	id = 'maltego.URL'
	displayName = 'URL'
	displayNamePlural = 'URLs'

	short_title = None # string short-title
	url = None # url url
	title = None # string title

	_fields = {
		'short_title': {'name': 'short-title', 'type': 'string', 'nullable': 'true'},
		'url': {'name': 'url', 'type': 'url', 'nullable': 'true'},
		'title': {'name': 'title', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, short_title=None, url=None, title=None, **kwargs):
		super().__init__(value, **kwargs)
		self.short_title = short_title
		self.url = url
		self.title = title

entities.entity_map[URL.id] = URL
