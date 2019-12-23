import ssl
import datetime

from tedious.entities import maltego
from tedious import Tedious, UIMessage, UIMessageType

app = Tedious(__name__)


@app.entity()
class Passphrase(maltego.Phrase):
	"""
	Like a phrase, but more secret
	"""
	
	id = 'custom.Passphrase'
	displayName = 'Passphrase'
	displayNamePlural = 'Passphrases'
	
	_fields = {}


@app.transform("helloTransform")
def hello_transform(phrase):
	"""
	Say hello
	"""
	return maltego.Phrase("Hello, " + phrase.value), \
		UIMessage("Hello UIMessage!", UIMessageType.PARTIAL_ERROR)


@app.transform("placeKitten")
def place_kitten(phrase, *, width="64", height="64"):
	"""
	Generate a placeholder kitten image from placekitten.com
	
	width: Image Width
	height: Image Height
	"""

	# We'll modify the existing Phrase object in-place
	phrase.icon_url = "http://placekitten.com/{}/{}".format(width, height)
	phrase.display_information["Birthday"] = "This kitten was born on <code>{}</code>.".format(datetime.datetime.now().isoformat())
	phrase.additional_fields["animal"] = "Kitten"
	phrase.weight = 1337
	
	return phrase


@app.transform("errorTransform")
def error_transform(phrase):
	"""
	Cause a python error to see what happens
	"""
	return variable_that_does_not_exist


@app.transform("fatalTransform")
def fatal_transform(phrase):
	"""
	Make a FatalError UIMessage from a phrase
	"""
	return UIMessage(phrase.text, UIMessageType.FATAL_ERROR)


context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('certificate.pem', 'key.pem')
app.run(host="0.0.0.0", port=31337, ssl_context=context)
