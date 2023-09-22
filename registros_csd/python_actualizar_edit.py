from suds.client import Client
import logging
import base64
 
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)
logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)
 
 
username = 'cclix@finkok.com.mx' # Usuario de Finkok
password = 'Legoland1953!'
RFC = 'IIA040805DZ4'
status = 'A' 
cer_path = "/home/ccalix/Documentos/csd_iia040805dz4_20230518062516/CSD_IIA040805DZ4_20230518062516/CSD_Sucursal_1_IIA040805DZ4_20230518_062510.cer"
cer_file = open(cer_path, 'rb').read()
cer_base64 = base64.b64encode(cer_file).decode('utf-8')

 
key_path = "/home/ccalix/Documentos/csd_iia040805dz4_20230518062516/CSD_IIA040805DZ4_20230518062516/CSD_Sucursal_1_IIA040805DZ4_20230518_062510.key"
cer_file = open(cer_path, 'rb').read()
cer_base64 = base64.b64encode(cer_file).decode('utf-8')
passphrase = '12345678a'
 
 
url = "https://demo-facturacion.finkok.com/servicios/soap/registration.wsdl"
client = Client(url,cache=None)#location=url
 
print (client.service.edit(username,password,RFC,status, cer_file, key_file, passphrase))