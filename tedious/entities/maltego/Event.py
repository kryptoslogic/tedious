# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="false" category="Events" conversionOrder="2147483647" description="An occurrence usually linked with a time and place" displayName="Event" displayNamePlural="Events" id="maltego.Event" largeIconResource="Event" smallIconResource="Event" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.Location</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="title" value="title">
	      <Fields>
	         <Field description="The event name" displayName="Title" hidden="false" name="title" nullable="true" readonly="false" type="string">
	            <SampleValue>Event</SampleValue>
	         </Field>
	         <Field description="The start of the event" displayName="Start Time" hidden="false" name="starttime" nullable="true" readonly="false" type="datetime" />
	         <Field description="The stop of the event" displayName="Stop Time" hidden="false" name="stoptime" nullable="true" readonly="false" type="datetime" />
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.Location import Location

class Event(Location):
	"""
	An occurrence usually linked with a time and place
	"""

	id = 'maltego.Event'
	displayName = 'Event'
	displayNamePlural = 'Events'

	title = None # string title
	starttime = None # datetime starttime
	stoptime = None # datetime stoptime

	_fields = {
		'title': {'name': 'title', 'type': 'string', 'nullable': 'true'},
		'starttime': {'name': 'starttime', 'type': 'datetime', 'nullable': 'true'},
		'stoptime': {'name': 'stoptime', 'type': 'datetime', 'nullable': 'true'},
	}

	def __init__(self, value, title=None, starttime=None, stoptime=None, **kwargs):
		super().__init__(value, **kwargs)
		self.title = title
		self.starttime = starttime
		self.stoptime = stoptime

entities.entity_map[Event.id] = Event
