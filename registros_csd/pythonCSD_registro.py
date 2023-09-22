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
RFC = 'XIQB891116QE4'
type_user = 'O'
coupon = ''
added = ''
cer_path = '/home/ccalix/Documentos/csd_xiqb891116qe4_20230509131448/CSD_XIQB891116QE4_20230509131448/xiqb891116qe4.cer'
cer_file = open(cer_path, 'rb').read()
cer_base64 = base64.b64encode(cer_file).decode('utf-8')
passphrase = '12345678a'
 
key_path ='/home/ccalix/Documentos/csd_xiqb891116qe4_20230509131448/CSD_XIQB891116QE4_20230509131448/CSD_Sucursal_1_XIQB891116QE4_20230509_131443.key'
key_file = open(key_path, 'rb').read()
key_base64 = base64.b64encode(key_file).decode('utf-8')
 
url = "https://demo-facturacion.finkok.com/servicios/soap/registration.wsdl"
client = Client(url,cache=None)#location=url
 
response = client.service.add(username,password,RFC, type_user, '', '',cer_file, key_file, passphrase)
print (response)