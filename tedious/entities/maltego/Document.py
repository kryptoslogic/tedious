# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Personal" conversionOrder="2147483647" description="A document on the Internet" displayName="Document" displayNamePlural="Documents" id="maltego.Document" largeIconResource="Document" smallIconResource="Document" visible="true">
	   <Properties displayValue="title" value="url">
	      <Fields>
	         <Field description="" displayName="Title" hidden="false" name="title" nullable="true" readonly="false" type="string">
	            <SampleValue>Some Document</SampleValue>
	         </Field>
	         <Field description="" displayName="Meta-Data" hidden="false" name="document.meta-data" nullable="true" readonly="false" type="string">
	            <SampleValue />
	         </Field>
	         <Field description="" displayName="URL" hidden="false" name="url" nullable="true" readonly="false" type="url" />
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities

class Document(entities.MaltegoEntity):
	"""
	A document on the Internet
	"""

	id = 'maltego.Document'
	displayName = 'Document'
	displayNamePlural = 'Documents'

	title = None # string title
	document_meta_data = None # string document.meta-data
	url = None # url url

	_fields = {
		'title': {'name': 'title', 'type': 'string', 'nullable': 'true'},
		'document_meta_data': {'name': 'document.meta-data', 'type': 'string', 'nullable': 'true'},
		'url': {'name': 'url', 'type': 'url', 'nullable': 'true'},
	}

	def __init__(self, value, title=None, document_meta_data=None, url=None, **kwargs):
		super().__init__(value, **kwargs)
		self.title = title
		self.document_meta_data = document_meta_data
		self.url = url

entities.entity_map[Document.id] = Document
