from src.clima import LecturaCSV
import getpass
import time

class Menu:
    
    def __init__(self):
        """Costructor de un menu, que iniciliza todas sus atributos de clase como diccionarios vacíos."""
        self.cache = {}
        self.errores = {}
        self.indice = {}

    def iniciar(self):
        """Guarda el resultadp de la funci+on leer.csv de la clase LecturaCSV en los atributos
        cache y errores de la clase.
        """
        clave = getpass.getpass("Introduce tu llave de Open Weather: ")
        datos = LecturaCSV.leer_csv('datasets/dataset1.csv', clave)
        self.cache  = datos[0]
        self.errores = datos[1]

    def revisar_datos(self):
        """Revisa que haya objetos en el cache o en los erroes, de no ser así termina el 
        programa
        """
        if self.cache.es_vacio() and self.errores.es_vacio():
            print("\nEl archivo está vacío\n")
            exit()
          
    def muestra_indice(self):
        """Muestra los indices de las ciudades, ademas recibe una entrada, con la que se 
        llama a  las funciones salir() y ver_errores(). Si el cache es vacío, entonces
        lo imprime y ofrece salir o ver los errores.
        """ 
        if not self.cache.objetos:
            self.espaciar()
            print("No hay ciudades para mostrar.\n")
            entrada = input("Introduce la letra r si deseas ver los errores o la letra z "
                            + "si deaseas salir: ").strip()
            self.ver_errores(entrada)
            self.salir(entrada)
            self.advertir_caracter()
            time.sleep(2)
            self.muestra_indice()
        ciudades = sorted(self.cache.objetos.keys())
        numero = 1
        self.espaciar()
        print("Índice: \n")
        for ciudad in ciudades:
            self.indice[numero] = ciudad
            print(" {0}.- {1}\n".format(numero, ciudad))
            numero += 1

    def seleccionar_ciudad(self):
        """Recibe una entrada, llama a la función salir() y ver_errores() con la entarda,si 
        esta es un número que pertenece al indice muestra el clima almacenado con esa llave,  
        de otra forma lanza una advetencia para que se ingrese un caracter válido.
        """
        entrada = input("Ingrese el índice de la ciudad cuyo clima desea " +
                       "consultar, la letra r para ver los errores o la letra " +
                       "z para salir: ").strip()
        self.salir(entrada)
        self.ver_errores(entrada)
        try:
            numero = int(entrada)
            if numero in self.indice:
                clima = self.cache.objetos[self.indice[numero]]
                self.espaciar()
                print(clima.to_string())
            else:     
                print("\nIntroduce un número válido\n")
                self.seleccionar_ciudad()
                return
            
        except ValueError:
            print("\nIntroduce un carácter válido\n")
            self.seleccionar_ciudad()
            return
     
    def finalizar(self):
        """Recibe una entrada con la que llama a la funcion salir(), si es el caracter i
        repite las funciones para seleccionar un indice", de otra manera imprime una advertencia
        y reinicia la funcion.
        """
        entrada = input('Si deseas regresar al índice introduce i' +
                ' o si deaseas salir introduce la tecla z: ').strip()
        self.salir(entrada)
        
        if entrada == "i":
            self.muestra_indice()
            self.seleccionar_ciudad()
            self.finalizar()
            return
        
        else:
            self.advertir_caracter()
            self.finalizar()
            return
     
    def ver_errores(self, entrada):
        """Si recibe "r" muestra en pantalla los errores y llama a la función finalizar."""      
        if entrada == "r":
            self.espaciar()
            self.errores.representar_errores()
            self.finalizar()
           
    def advertir_numero(self):
        """Imprime en pantalla que se seleccione un numero valido."""
        print("\nIntroduce un número válido.\n")
        
    def advertir_caracter(self):
        """Imprime en pantalla que se seleccione un caracter valido"""
        print("\nIntroduce un carácter válido\n")
            
    def salir(self, entrada):
        """Si recibe el carácter z termina el programa"""
        if entrada == "z":
            exit()
            
    def espaciar(self):
        """Crea espacios en pantalla para una mejor visibilidad"""
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
