import base64

# Nombre del archivo que deseas convertir
nombre_archivo = '/home/ccalix/Documentos/soporte_tecnico/csd_eku9003173c9_20230517223903/CSD_EKU9003173C9_20230517223903/CSD_Sucursal_1_EKU9003173C9_20230517_223850.enc'

try:
    # Abre el archivo en modo lectura binaria
    with open(nombre_archivo, 'rb') as archivo:
        # Lee el contenido del archivo
        contenido = archivo.read()
        
        # Codifica el contenido en Base64
        contenido_base64 = base64.b64encode(contenido).decode('utf-8')
        
        # Imprime la cadena en Base64
        print(contenido_base64)
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se encontró.")
except Exception as e:
    print(f"Ocurrió un error: {str(e)}")
