from src.clima import LecturaCSV
from src.clima import config
import pytest

def test_leer_sin_archivo(tmpdir):
    """"""
    fpath = f"{tmpdir}/test.txt"
    
    with pytest.raises(SystemExit):
        LecturaCSV.leer_csv(fpath,"0")

def test_leer_formato_incorrecto(tmpdir):
    fpath = f"{tmpdir}/test.txt"
    
    with open(fpath, "x") as file:
        file.write("1,1,1,1")
        datos = LecturaCSV.leer_csv(fpath,config.api_key)
        cache = datos[0]
        errores = datos[1]
        assert(cache.es_vacio())
        assert(errores.es_vacio())
        
def test_leer_solo_errores(tmpdir):
    fpath = f"{tmpdir}/test.txt"
          
    with open(fpath, "x") as file:
        file.write("destination_latitude,destination_longitude\n")
        file.write("TLC,MTY\n")
        file.write("300.20,1000.90\n")
        file.write("TLC,MTY\n")
    
    with open(fpath, "r") as file:
        datos = LecturaCSV.leer_csv(fpath,config.api_key)
        cache = datos[0]
        errores = datos[1]
        assert(cache.es_vacio())
        assert(errores.get_longitud() == 2)
        
def test_leer_solo_aciertos(tmpdir):  
    fpath = f"{tmpdir}/test.txt"
    
    with open(fpath, "x") as file:
        file.write("destination_latitude,destination_longitude\n")
        file.write("20.52,-103.31\n")
        file.write("20.52,-103.31\n")
        file.write("19.4363,-99.0721\n")
        
    with open(fpath, "r") as file:
        datos = LecturaCSV.leer_csv(fpath,config.api_key)
        cache = datos[0]
        errores = datos[1]
        assert(cache.get_longitud() == 2)
        assert(errores.es_vacio())


    
    
    
    
    
     


        
    