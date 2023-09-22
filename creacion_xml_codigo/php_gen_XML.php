<?php
 
$username = 'ccalix@finkok.com.mx'; # Usuario de Finkok
$password = 'Legoland1953!'; # Contraseña de Finkok
$uuid = '7ED34E9C-9B8E-5BFC-96A3-576C5A04CDB8'; # UUID del cual se desea obtener el XML
$rfc = 'EKU9003173C9'; # RFC emisor del comprobante
$invoice_type = 'I'; # ('I' CFDI, 'R' Retentions)

# Conexión al web service de Utilities (Get_xml)
$url = "https://demo-facturacion.finkok.com/servicios/soap/utilities.wsdl";
$client = new SoapClient($url);
 
# Se almacenan las variables con los datos en el array $params  
$params = array(
  "username" => $username,
  "password" => $password,
  "uuid" => $uuid,
  "taxpayer_id" => $rfc,
  "invoice_type" => $invoice_type
);
 
# El array $params envía los parámetros al método get_xml del web service de Utilities
$response = $client->__soapCall("get_xml", array($params)); # La variable $response obtiene la respuesta del web service

# Generación de archivo .xml con la respuesta del web service
$file = fopen("get_xml.xml", "a");
fwrite($file, $response->get_xmlResult->xml);
fclose($file);
 
?>