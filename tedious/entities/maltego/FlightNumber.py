# The contents of this file have been autogenerated. Edit at your own risk!!!
# Despite this, it *is* intended to be human readable.

"""
.. highlight:: xml
.. code-block:: xml

	<MaltegoEntity allowedRoot="true" category="Tracking" conversionOrder="2147483647" description="A number, when combined with the name of the airline and the date, that identifies a particular flight" displayName="Flight Number" displayNamePlural="Flight Numbers" id="maltego.FlightNumber" largeIconResource="FlightNumber" smallIconResource="FlightNumber" visible="true">
	   <Properties displayValue="flight.id" value="flight.id">
	      <Fields>
	         <Field description="The airline and number of the flight" displayName="Flight ID" evaluator="maltego.replace" hidden="false" name="flight.id" nullable="true" readonly="false" type="string">
	            <DefaultValue>$trim($property(flight.airline) $property(flight.number))</DefaultValue>
	            <SampleValue />
	         </Field>
	         <Field description="The flight number" displayName="Flight Number" hidden="false" name="flight.number" nullable="true" readonly="false" type="string">
	            <SampleValue>SA203</SampleValue>
	         </Field>
	         <Field description="The airline of the flight" displayName="Airline" hidden="false" name="flight.airline" nullable="true" readonly="false" type="string">
	            <SampleValue>South African Airways</SampleValue>
	         </Field>
	         <Field description="The flight date" displayName="Date" hidden="false" name="flight.date" nullable="true" readonly="false" type="date" />
	      </Fields>
	   </Properties>
	</MaltegoEntity>

"""

import tedious.entities as entities

class FlightNumber(entities.MaltegoEntity):
	"""
	A number, when combined with the name of the airline and the date, that identifies a particular flight
	"""

	id = 'maltego.FlightNumber'
	displayName = 'Flight Number'
	displayNamePlural = 'Flight Numbers'

	flight_id = None # string flight.id
	flight_number = None # string flight.number
	flight_airline = None # string flight.airline
	flight_date = None # date flight.date

	_fields = {
		'flight_id': {'name': 'flight.id', 'type': 'string', 'nullable': 'true'},
		'flight_number': {'name': 'flight.number', 'type': 'string', 'nullable': 'true'},
		'flight_airline': {'name': 'flight.airline', 'type': 'string', 'nullable': 'true'},
		'flight_date': {'name': 'flight.date', 'type': 'date', 'nullable': 'true'},
	}

	def __init__(self, value, flight_id=None, flight_number=None, flight_airline=None, flight_date=None, **kwargs):
		super().__init__(value, **kwargs)
		self.flight_id = flight_id
		self.flight_number = flight_number
		self.flight_airline = flight_airline
		self.flight_date = flight_date

entities.entity_map[FlightNumber.id] = FlightNumber
