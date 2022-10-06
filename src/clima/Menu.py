from src.clima import LecturaCSV
import getpass
import time

class Menu:
    
    def __init__(self):
        self.cache = {}
        self.errores = {}
        self.indice = {}

    def iniciar(self):
        clave = getpass.getpass("Introduce tu llave de Open Weather: ")
        datos = LecturaCSV.leer_csv('datasets/dataset1.csv', clave)
        self.cache  = datos[0]
        self.errores = datos[1]

    def revisar_datos(self):
        if self.cache.es_vacio() and self.errores.es_vacio():
            print("\nEl archivo está vacío\n")
            exit()
            
    def muestra_indice(self):
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
        if entrada == "r":
            self.espaciar()
            self.errores.representar_errores()
            self.finalizar()
            
    def advertir_numero(self):
        print("\nIntroduce un número válido.\n")
        
    def advertir_caracter(self):
        print("\nIntroduce un carácter válido\n")
            
    def salir(self, entrada):
        if entrada == "z":
            exit()
            
    def espaciar(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
