"""Modulo principal del proyecto 1. Lleva a cabo el programa para 
obtener el clima de las ciudades de destino en los tickets de 
aeropuerto dentro de un archivo csv."""

from src.clima.Menu import Menu 

menu = Menu()
menu.iniciar()
menu.revisar_datos()
menu.muestra_indice()
menu.seleccionar_ciudad()
menu.finalizar()

