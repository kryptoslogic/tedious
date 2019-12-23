# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Events" conversionOrder="2147483647" description="A telephonic conversation" displayName="Conversation (Phone)" displayNamePlural="Conversations (Phone)" id="maltego.ConversationPhone" largeIconResource="PhoneConversation" smallIconResource="PhoneConversation" visible="true">
	   <BaseEntities>
	      <BaseEntity>maltego.Conversation</BaseEntity>
	   </BaseEntities>
	   <Properties displayValue="">
	      <Fields>
	         <Field description="The phone number of the caller" displayName="Caller Number" hidden="false" name="phonenumber.caller" nullable="true" readonly="false" type="string">
	            <SampleValue />
	         </Field>
	         <Field description="The phone number of the callee" displayName="Callee Number" hidden="false" name="phonenumber.callee" nullable="true" readonly="false" type="string">
	            <SampleValue />
	         </Field>
	         <Field description="The start of the conversation" displayName="Start time" hidden="false" name="starttime" nullable="true" readonly="false" type="datetime" />
	         <Field description="The duration of the conversation" displayName="Duration" hidden="false" name="duration" nullable="true" readonly="false" type="timespan" />
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities
from tedious.entities.maltego.Conversation import Conversation

class ConversationPhone(Conversation):
	"""
	A telephonic conversation
	"""

	id = 'maltego.ConversationPhone'
	displayName = 'Conversation (Phone)'
	displayNamePlural = 'Conversations (Phone)'

	phonenumber_caller = None # string phonenumber.caller
	phonenumber_callee = None # string phonenumber.callee
	starttime = None # datetime starttime
	duration = None # timespan duration

	_fields = {
		'phonenumber_caller': {'name': 'phonenumber.caller', 'type': 'string', 'nullable': 'true'},
		'phonenumber_callee': {'name': 'phonenumber.callee', 'type': 'string', 'nullable': 'true'},
		'starttime': {'name': 'starttime', 'type': 'datetime', 'nullable': 'true'},
		'duration': {'name': 'duration', 'type': 'timespan', 'nullable': 'true'},
	}

	def __init__(self, value, phonenumber_caller=None, phonenumber_callee=None, starttime=None, duration=None, **kwargs):
		super().__init__(value, **kwargs)
		self.phonenumber_caller = phonenumber_caller
		self.phonenumber_callee = phonenumber_callee
		self.starttime = starttime
		self.duration = duration

entities.entity_map[ConversationPhone.id] = ConversationPhone