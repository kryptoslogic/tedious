# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Personal" conversionOrder="50" description="Entity representing a human" displayName="Person" displayNamePlural="People" id="maltego.Person" largeIconResource="Person" smallIconResource="Person" visible="true">
	   <Converter>
	      <Value>([A-Z]{1,15}[a-z]{0,15}) ([A-Z]{0,15}[a-z]{0,15} *[A-Z]{0,15}[a-z]{0,15} *[A-Z]{0,15}[a-z]{0,15})</Value>
	      <RegexGroups>
	         <RegexGroup property="person.firstnames" />
	         <RegexGroup property="person.lastname" />
	      </RegexGroups>
	   </Converter>
	   <Properties displayValue="person.fullname" value="person.fullname">
	      <Groups />
	      <Fields>
	         <Field description="" displayName="Full Name" evaluator="maltego.replace" hidden="false" name="person.fullname" nullable="true" readonly="false" type="string">
	            <DefaultValue>$trim($property(person.firstnames) $property(person.lastname))</DefaultValue>
	            <SampleValue />
	         </Field>
	         <Field description="" displayName="First Names" hidden="false" name="person.firstnames" nullable="true" readonly="false" type="string">
	            <SampleValue>John</SampleValue>
	         </Field>
	         <Field description="" displayName="Surname" hidden="false" name="person.lastname" nullable="true" readonly="false" type="string">
	            <SampleValue>Doe</SampleValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities

class Person(entities.MaltegoEntity):
	"""
	Entity representing a human
	"""

	id = 'maltego.Person'
	displayName = 'Person'
	displayNamePlural = 'People'

	person_fullname = None # string person.fullname
	person_firstnames = None # string person.firstnames
	person_lastname = None # string person.lastname

	_fields = {
		'person_fullname': {'name': 'person.fullname', 'type': 'string', 'nullable': 'true'},
		'person_firstnames': {'name': 'person.firstnames', 'type': 'string', 'nullable': 'true'},
		'person_lastname': {'name': 'person.lastname', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, person_fullname=None, person_firstnames=None, person_lastname=None, **kwargs):
		super().__init__(value, **kwargs)
		self.person_fullname = person_fullname
		self.person_firstnames = person_firstnames
		self.person_lastname = person_lastname

entities.entity_map[Person.id] = Person
