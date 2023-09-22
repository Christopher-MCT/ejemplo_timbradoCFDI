import os
import base64
import hashlib
from datetime import datetime
from lxml import etree
from suds.client import Client
from M2Crypto.RSA import load_key_string

class CrearCadena40:
    def __init__(self):
        self.now = datetime.now().replace(microsecond=0).isoformat('T')
        with open('/home/ccalix/Descargas/cfdi_40_2022/xslt/cadenaoriginal_4_0.xslt', 'rb') as xslt_file:
            XSLT = xslt_file.read()
        XSLT_STYLEDOC = etree.XML(XSLT)
        self.XSLT_STYLE = etree.XSLT(XSLT_STYLEDOC)

        with open('/home/ccalix/Documentos/soporte_tecnico/creacion_xml_codigo/ejemplo_cancelacion_01/xml_ej_01.xml', 'rb') as xml_file:
            self.xml_string = xml_file.read()
        
        xml_etree = etree.fromstring(self.xml_string)
        cadena_original = self.cadena_original40(self.xml_string, xml_etree)
        print("--------------CADENA ORIGINAL-----------------")
        print(cadena_original)
        sello = self.sello40(cadena_original)
        xml_etree = etree.fromstring(self.xml_string)
        xml_etree.set('Sello', sello)
        xml_string = etree.tostring(xml_etree, encoding='UTF-8')
        print("--------------SELLO-----------------")
        print(sello)

    def cadena_original40(self, xml_string, xml_etree):
        xml_string = xml_string.decode('utf-8')
        result = self.XSLT_STYLE(xml_etree)
        original_string = str(result)
        original_string = original_string.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '')
        original_string = original_string.replace('\n','')
        original_string = original_string.replace('&quot;', '"')
        original_string = original_string.replace('&lt;', '<')
        original_string = original_string.replace('&gt;', '>')
        original_string = original_string.replace('&apos;', '´')
        original_string = original_string.replace('&amp;', '&')
        original_string = original_string.strip()
        return original_string

    def sello40(self, cadena_original):
        self.key_pem = open('key.pem', 'rb').read()

        rsa = load_key_string(self.key_pem)
        assert len(rsa) in (1024, 2048)
        assert rsa.e == b'\x00\x00\x00\x03\x01\x00\x01'
        # The algorithm was changed from MD5 to SHA256
        md5_digest = hashlib.sha256(cadena_original.encode('utf-8')).digest()
        rsa_signature = rsa.sign(md5_digest, 'sha256')
        signature = base64.b64encode(rsa_signature)
        return signature

CrearCadena40()
