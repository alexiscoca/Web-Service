import csv
from src.clima.Clima import Clima
from src.clima.Errores import Errores_coordenadas as Errores
from src.clima.Cache import Cache
from src.clima import Peticiones


def leer_csv(nombre_archivo, llave):
    """Lee un archivo csv de tickets. 
    
    Por cada par de coordenadas de la ciudad de destino realiza una 
    petición y almacena el resultado en un objeto clima antes de 
    agregarlo a un cache al obtener una respuesta satisfactoria, o 
    en los errores de otro modo.

    Parámetros:
        nombre_archivo (str) -- El nombre del archivo csv de tickets
        que se quiere leer.

        llave -- La llave de para utilizar la API de OpenWather.   
    """
    cache_coordenadas = Cache()
    cache_climas = Cache()
    errores = Errores()
    
    try:
        with open(nombre_archivo, 'r') as archivo:
            lector = csv.DictReader(archivo)
            for linea in lector:
                try:
                    lat_dest = round(float(linea['destination_latitude']),2)
                    lon_dest = round(float(linea['destination_longitude']),2)
                except:
                    errores.agrega((linea['destination_latitude'], 
                                    linea['destination_longitude']), None)
                    continue
                cache_coordenadas.agrega((lat_dest, lon_dest),{})
            for coordenadas in cache_coordenadas.objetos.keys():
                latitud = coordenadas[0]
                longitud = coordenadas[1]
                datos = Peticiones.enviar_peticion(latitud, longitud, llave)
                if not datos:
                    errores.agrega((latitud, longitud),None)
                else:
                    clima = Clima(datos)
                    cache_climas.objetos[clima.ciudad.nombre] = clima
                    
        return (cache_climas, errores)
    except FileNotFoundError:
        print("\nNo fue posible leer el archivo.\n")
        exit()