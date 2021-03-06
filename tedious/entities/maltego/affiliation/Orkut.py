# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="false" conversionOrder="2147483647" description="Membership of the Orkut social network" displayName="Affiliation - Orkut" displayNamePlural="Affiliations - Orkut" id="maltego.affiliation.Orkut" largeIconResource="Orkut">
	   <BaseEntities>
	      <BaseEntity>maltego.Affiliation</BaseEntity>
	   </BaseEntities>
	   <Properties>
	      <Fields>
	         <Field displayName="Network" hidden="false" name="affiliation.network" nullable="true" readonly="true" type="string">
	            <DefaultValue>Orkut</DefaultValue>
	         </Field>
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

from tedious.entities.maltego.Affiliation import Affiliation

class Orkut(Affiliation):
	"""
	Membership of the Orkut social network
	"""

	id = 'maltego.affiliation.Orkut'
	displayName = 'Affiliation - Orkut'
	displayNamePlural = 'Affiliations - Orkut'

	affiliation_network = None # string affiliation.network

	_fields = {
		'affiliation_network': {'name': 'affiliation.network', 'type': 'string', 'nullable': 'true'},
	}

	def __init__(self, value, affiliation_network=None, **kwargs):
		super().__init__(value, **kwargs)
		self.affiliation_network = affiliation_network
