# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" conversionOrder="2147483647" description="Web site directory" displayName="Web Dir" displayNamePlural="Web Dirs" id="maltego.WebDir" largeIconResource="WebDir">
	   <Properties value="directory.name">
	      <Fields>
	         <Field displayName="Name" hidden="false" name="directory.name" nullable="true" readonly="false" type="string">
	            <DefaultValue>admin</DefaultValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities

class WebDir(entities.MaltegoEntity):
	"""
	Web site directory
	"""

	id = 'maltego.WebDir'
	displayName = 'Web Dir'
	displayNamePlural = 'Web Dirs'

	directory_name = None # string directory.name

	_fields = {
		'directory_name': {'name': 'directory.name', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, directory_name=None, **kwargs):
		super().__init__(value, **kwargs)
		self.directory_name = directory_name
