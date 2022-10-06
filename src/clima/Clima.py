import datetime
from src.clima.Ciudad import Ciudad
from src.clima import Maneja_Cadenas

class Clima:
    def __init__(self, datos):
        self.ciudad = Ciudad(datos)
        self.tiempo = datetime.datetime.now().time().strftime("%H:%M:%S")
        self.tipo = Maneja_Cadenas.iniciar_con_mayuscula(
            datos["weather"][0]["description"])
        self.sensacion = datos["main"]["feels_like"]
        self.viento = datos["wind"]["speed"]
        self.humedad = datos["main"]["humidity"]
        self.visibilidad = int(datos["visibility"])/1000
        self.presion = datos["main"]["pressure"]
        self.temperatura_max = datos["main"]["temp_max"]
        self.temperatura_min = datos["main"]["temp_min"]

    def to_string(self):
        """Representa en cadena a un clima, un atributo por linea.
        
        Regresa:
        
        cadena (str) -- La representación del clima.
        """
        cadena = (self.ciudad.to_string() +
                 "Tiempo actual: {0}\n" + 
                 "Clima: {1}\n" +
                 "Sensación térmica: {2}°\n" +
                 "Viento: {3} km/h\n" +
                 "Humedad: {4}%\n" +
                 "Visibilidad: {5} km\n" +
                 "Presión: {6} mbar\n" +
                 "Temperatura: \n" + 
                 " -Máxima: {7}°\n" + 
                 " -Miníma: {8}°\n").format(
                  self.tiempo, self.tipo, self.sensacion, self.viento, self.humedad,
                  self.visibilidad, self.presion, self.temperatura_max,
                  self.temperatura_min)
        return cadena 