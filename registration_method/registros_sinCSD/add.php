<?php
 
# Username and Password, assigned by FINKOK
$username = 'ccalix@finkok.com.mx';
$password = 'Legoland1953!';
$rfc = 'AAD990814BP7';
 
 
$url = "https://demo-facturacion.finkok.com/servicios/soap/registration.wsdl";
$client = new SoapClient($url, array('trace' => 1));
 
$params = array(
  "reseller_username" => $username,
  "reseller_password" => $password,
  "taxpayer_id" => $rfc
);
$response = $client->__soapCall("add", array($params));
echo "REQUEST:\n" . $client->__getLastRequest() . "\n";
print_r($response);
 
?>