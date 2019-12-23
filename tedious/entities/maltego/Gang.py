# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Groups" conversionOrder="2147483647" description="An organized group of criminals" displayName="Gang" displayNamePlural="Gangs" id="maltego.Gang" largeIconResource="Gang" smallIconResource="Gang" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.Organization</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="title" value="title">
	      <Fields>
	         <Field description="Name of the gang" displayName="Name" hidden="false" name="title" nullable="true" readonly="false" type="string">
	            <SampleValue>Latin Kings</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.Organization import Organization

class Gang(Organization):
	"""
	An organized group of criminals
	"""

	id = 'maltego.Gang'
	displayName = 'Gang'
	displayNamePlural = 'Gangs'

	title = None # string title

	_fields = {
		'title': {'name': 'title', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, title=None, **kwargs):
		super().__init__(value, **kwargs)
		self.title = title

entities.entity_map[Gang.id] = Gang
