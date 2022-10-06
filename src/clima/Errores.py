class Errores_coordenadas:
    """Clase para manejar las coordenadas de las que no haya podido 
    obtener información mediante la API.
    
    Atributos de clase:
    
        lista (list) -- Una lista de tuplas que contienen las coordenadas
        sin información.
    """
    
    def __init__(self):
        """Constructor que inicializa el atributo objetos como un 
        diccionario vacío."""
        self.objetos = {}
    
    def agrega(self, llave, valor):
        """Agrega una llave con su valor a los errores, solo si está no 
        se encontraba ya.

        Parámetros:
            llave -- La llave del con la que se podra accesar al valor.

            valor -- El valor que se quiere almacenar en el cache.
        """
        if not llave in self.objetos:
            self.objetos[llave] = valor
            
    def es_vacio(self):
        """Regresa si es verdad que no hay errores.
        
        Regresa:
            True -- Si no hay errores.

            False -- Si hay errores.
        """
        if self.objetos:
            return False
        return True
    
    def get_longitud(self):
        """Regresa la longitud del diccionario objetos.
            
        Regresa:
            longitud (int) -- La longitud del atributo de clase objetos.
        """
        return len(self.objetos)
    
    def representar_errores(self):
        """Imprime la representación en cadena de todos los errores"""
        if not self.objetos:
            print("No hay errores\n")
        else:
            print("Las coordenas de las que no se pudo obtener información son:\n")
            for coordenadas in self.objetos.keys():
                error = " Lat: {lt}, Lon: {ln}\n".format(
                                lt = coordenadas[0], ln = coordenadas[1])
                print(error)