#!/usr/bin/python
 
from zeep import Client
import logging
import base64
from lxml import etree
from zeep.plugins import HistoryPlugin
 
logging.basicConfig(level=logging.INFO)
logging.getLogger('zeep.client').setLevel(logging.DEBUG)
logging.getLogger('zeep.transport').setLevel(logging.DEBUG)
logging.getLogger('zeep.xsd.schema').setLevel(logging.DEBUG)
logging.getLogger('zeep.wsdl').setLevel(logging.DEBUG)
 
# Username and Password, assigned by FINKOK
username = 'ccalix@finkok.com.mx'
password = 'Legoland1953!!'
 
# Read the xml file and encode it to bytes
history = HistoryPlugin()
invoice_path = "/home/ccalix/Documentos/soporte_tecnico/example.xml"
file = open(invoice_path)
lines = "".join(file.readlines())
xml = lines.encode("UTF-8")
 
# Consuming the stamp service
url = "https://demo-facturacion.finkok.com/servicios/soap/stamp.wsdl"
client = Client(wsdl = url, plugins = [history])
contenido = client.service.sign_stamp(xml, username, password)
xml = contenido.xml
print(contenido) 
 
# Get stamped xml
archivo = open("stamp.xml","w")
archivo.write(str(xml))
archivo.close()
 
# Get SOAP Request
request = etree.tostring(history.last_sent["envelope"])
req_file = open('/home/ccalix/Documentos/soporte_tecnico/envolturas/request.xml', 'w') 
req_file.write(request.decode("UTF-8") )
req_file.close()
 
# Get SOAP Response 
response = etree.tostring(history.last_received["envelope"])
res_file = open('/home/ccalix/Documentos/soporte_tecnico/envolturas/response.xml', 'w')
res_file.write(response.decode("UTF-8") )
res_file.close()