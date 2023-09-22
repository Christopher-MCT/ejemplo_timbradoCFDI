from suds.client import Client
import logging
import base64
 
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)
logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)
 
# Username y Password de Finkok
username = 'ccalix@finkok.com.mx'
password = 'Legoland1953!'
RFC = 'XAXX010101000'
 
# Consumir el método add del web services de registration
url = "https://demo-facturacion.finkok.com/servicios/soap/registration.wsdl"
client = Client(url,cache=None)#location=url
 
print (client.service.add(username,password,RFC))