class Cache:
    """Clase para representar un cache, el cual sirve para almacenar información
    sin repetir y poder consultarlos.
    
    Atributos de clase:
        objetos -- Un diccionario para almacenar la información.
    """
    
    def __init__(self):
        """Constructor de un cache que inicializa el atributo
        objetos como un diccionario vacío."""
        self.objetos = {}
    
    def agrega(self, llave, valor):
        """Agrega una llave con su valor al cache, solo si está no se encontraba ya.

        Parámetros:
            llave -- La llave del con la que se podra accesar al valor.

            valor -- El valor que se quiere almacenar en el cache.
        """
        if not llave in self.objetos:
            self.objetos[llave] = valor
            
    def es_vacio(self):
        """Regresa si es verdad que el caché está vacío.
        
        Regresa:
            True -- Si el cache está vacío.

            False -- Si el cache contiene algo.
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