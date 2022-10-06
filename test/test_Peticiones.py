from src.clima import Peticiones
from src.clima import config
        
def test_peticiones():
    respuesta = Peticiones.enviar_peticion(1000.10,200.123, config.api_key)
    assert(not respuesta)
    respuesta = Peticiones.enviar_peticion(20.52,-103.31, config.api_key)
    assert(respuesta)