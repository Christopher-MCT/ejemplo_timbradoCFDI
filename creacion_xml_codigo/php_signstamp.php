<?php
 
$username = 'ccalix@finkok.com.mx'; # Usuario de Finkok
$password = 'Legoland1953!'; # Contraseña de Finkok

# Leer el archivo xml y codificarlo en la base 64
$invoice_path = "/home/ccalix/Documentos/soporte_tecnico/creacion_xml_codigo/get_xml.xml";
$xml_file = fopen($invoice_path, "rb");
$xml_content = fread($xml_file, filesize($invoice_path));
fclose($xml_file);
 
# Se almacenan las variables con los datos en el array $params
$params = array(
"xml" => $xml_content,
"username" => $username,
"password" => $password
);
 
# Petición al web service
$client = new SoapClient("https://demo-facturacion.finkok.com/servicios/soap/stamp.wsdl", array('trace' => 1));
$result = $client->__soapCall("sign_stamp", array($params));
# Imprimir la respuesta del web service en pantalla
#echo "REQUEST:\n" . $client->__getLastRequest() . "\n";
$request = $client->__getLastRequest();
$response = $client->__getLastResponse();
 
print_r($request);
print_r($response);
 
# Generación de archivo .xml con el Request de timbrado
$file = fopen("/home/ccalix/Documentos/soporte_tecnico/creacion_xml_codigo/peticionesTimbrado/SoapRequest.xml", "a");
fwrite($file, $client->__getLastRequest() . "\n");
fclose($file);
 
$file = fopen("/home/ccalix/Documentos/soporte_tecnico/creacion_xml_codigo/peticionesTimbrado/SoapResponse.xml", "a");
fwrite($file, $client->__getLastResponse() . "\n");
fclose($file);
 
?>