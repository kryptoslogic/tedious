from tedious import entities
from tedious.entities import maltego
import lxml.etree as ET

foobar = maltego.IPv4Address("8.8.8.8")
foobar.ipaddress_internal = False

xml = foobar.to_xml()

print(ET.tostring(xml, pretty_print=True).decode())

res = maltego.IPv4Address.from_xml(xml)
print(res)
print(res.value)
print(res.ipaddress_internal)

leader = maltego.GangLeader("El Chapo", person_lastname="Chapo")
print(leader.person_lastname)
xml = leader.to_xml()
print(ET.tostring(xml, pretty_print=True).decode())
