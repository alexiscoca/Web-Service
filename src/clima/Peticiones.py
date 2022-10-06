import requests

def enviar_peticion(lat, lon, llave):
    """Realiza una petición a la API de OpenWather con las coordenadas y
    la llave recibidas.
    
    Parámetros:
        lat -- La latitud de las coordenadas que definen la ubicación
        de una ciudad.

        lon -- La longitud de las coordenadas que definen la ubicación
        de una ciudad.
            
        llave -- La llave que otorga OpenWeather para consumir su API.
    """
    url = (("https://api.openweathermap.org/data/2.5/weather?lat={lt}&lon={ln}" +
          "&appid={key}&lang=es&units=metric").format(lt = lat,ln = lon, key = llave))
    response = requests.get(url)
    if response.status_code == 200:
        return  response.json()
    else:
        return {}

