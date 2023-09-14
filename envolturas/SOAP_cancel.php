<?php
 
#phpinfo();

 
$username = 'ccalix@finkok.com.mx';
$password = 'Legoland1953!';
$taxpayer = 'EKU9003173C9';
 
# Read the x509 certificate file on PEM format and encode it on base64
$cer_path = "/home/ccalix/Documentos/soporte_tecnico/csd_eku9003173c9_20230517223903/CSD_EKU9003173C9_20230517223903/CSD_Sucursal_1_EKU9003173C9_20230517_223850.pem"; 
$cer_file = fopen($cer_path, "r");
$cer_content = fread($cer_file, filesize($cer_path));
fclose($cer_file);
# In newer PHP versions the SoapLib class automatically converts FILE parameters to base64, so the next line is not needed, otherwise uncomment it
#$cer_content = base64_encode($cer_content);

# Read the Encrypted Private Key (des3) file on PEM format and encode it on base64
$key_path = "/home/ccalix/Documentos/soporte_tecnico/csd_eku9003173c9_20230517223903/CSD_EKU9003173C9_20230517223903/CSD_Sucursal_1_EKU9003173C9_20230517_223850.enc";
$key_file = fopen($key_path, "r");
$key_content = fread($key_file,filesize($key_path));
fclose($key_file);
# In newer PHP versions the SoapLib class automatically converts FILE parameters to base64, so the next line is not needed, otherwise uncomment it
#$key_content = base64_encode($key_content);

$client = new SoapClient("https://demo-facturacion.finkok.com/servicios/soap/cancel.wsdl", array('trace' => 1));
 
$uuids = array("UUID" => "7ED34E9C-9B8E-5BFC-96A3-576C5A04CDB8", "Motivo" => "02", "FolioSustitucion" => "");
$uuid_ar = array('UUID' => $uuids);
$uuids_ar = array('UUIDS' => $uuid_ar);
print_r($uuids_ar);
 
$params = array("UUIDS"=>$uuid_ar,
                "username" => $username,
                "password" => $password,
                "taxpayer_id" => $taxpayer,
                "cer" => $cer_content,
                "key" => $key_content);
 
print_r($params);
 
$response = $client->__soapCall("cancel", array($params));
 
# Generación de archivo .xml con el Request de timbrado
$file = fopen("/home/ccalix/Documentos/soporte_tecnico/envolturas/SoapRequest.xml", "a");
fwrite($file, $client->__getLastRequest() . "\n");
fclose($file);
 
$file = fopen("/home/ccalix/Documentos/soporte_tecnico/envolturas/SoapResponse.xml", "a");
fwrite($file, $client->__getLastResponse() . "\n");
fclose($file);
 
?>