# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="false" description="An informational message, typical log() or status()" displayName="Machine Information" id="maltego.MachineInfoAction" largeIconResource="SpeechBubble" visible="false">
	   <BaseEntities>
	      <BaseEntity>maltego.MachineAction</BaseEntity>
	   </BaseEntities>
	</MaltegoEntity>

"""

from tedious.entities.maltego.MachineAction import MachineAction

class MachineInfoAction(MachineAction):
	"""
	An informational message, typical log() or status()
	"""

	id = 'maltego.MachineInfoAction'
	displayName = 'Machine Information'
	displayNamePlural = None


	_fields = {
	}

	def __init__(self, value, **kwargs):
		super().__init__(value, **kwargs)
