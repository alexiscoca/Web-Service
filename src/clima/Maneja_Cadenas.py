"""Contiene funciones para cambiar el formato de cadenas (str)."""

def iniciar_con_mayuscula(palabra):
    """Cambia la primera letra de una palabra a mayúscula.
    
    Parámetros:
        palabra (str) -- La palabra que se quiere modificar.
    """
    return palabra.replace(palabra[0],palabra[0].upper())