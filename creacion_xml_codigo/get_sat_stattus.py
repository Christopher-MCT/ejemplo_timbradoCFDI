#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from suds.client import Client
import logging
import base64
 
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
#logging.getLogger('suds.transport').setLevel(logging.DEBUG)
#logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
#logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)
 
username='ccalix@finkok.com.mx' # usuario proporcionado por la plataforma de Finkok. Tipo String
password='Legoland1953!' # La lcontraseña proporcionada por la plataforma Finkok.Tipo String
taxpayer_id='EKU9003173C9'# El rfc emisor de las facturas a consultar Tipo String 
rtaxpayer_id='CUSC850516316' #El rfc receptorde los CFDI a consultar Tipo String
uuid='7ED34E9C-9B8E-5BFC-96A3-576C5A04CDB8' # El UUID del CFDI a consultar  Tipo Sring
total='5999.99' # El valor del aributo total del CFDI
 
url = "https://demo-facturacion.finkok.com/servicios/soap/cancel.wsdl"
client = Client(url,cache=None)#location=url
 
print (client.service.get_sat_status(username,password,taxpayer_id, rtaxpayer_id, uuid, total))