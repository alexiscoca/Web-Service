class Ciudad:
    """"Clase para representar una ciudad.
    
    Atributos de clase:
        nombre -- El nombre de la ciudad.
        
        latitud -- Latitud de las coordenadas que determinan la ubicación 
        de la ciudad.
        
        longitud -- Longitud de las coordenadas que determinan la ubicación 
        de la ciudad.
    """

    def __init__(self, datos):
        """Constructor de una ciudad que inicializa sus atributos con los 
        datos recibe.
        
        Parámetros:
        
        datos (dict) -- Información de una ciudad. Contiene las llaves
        "name" y "coord", cuyos valores son el nombre y las coordebadas
        de la ciudad respectivamente. Las coordenadas estarán dadas 
        como un diccionario, en el cual sus claves serán "lat" y 
        "lon" y sus respectivos valores la latitud y longitud de la 
        ciudad.  
        """
        self.nombre = datos["name"]
        self.latitud = datos["coord"]["lat"]
        self.longitud = datos["coord"]["lon"]

    def to_string(self):
        """Representa en cadena a una ciudad, un atributo por linea.
        
        Regresa:
        
        cadena (Str) -- La representación de la ciudad.
        """
        cadena = ("Ciudad: {0}\n" +
                  "Coordenas:\n" + 
                  " -Latitud: {1}°\n" +
                  " -Longitud: {2}°\n").format(
                    self.nombre, self.latitud,self.longitud)
        return cadena 
     