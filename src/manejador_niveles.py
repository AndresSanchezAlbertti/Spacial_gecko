from class_nivel_uno import *
from class_nivel_dos import *

class Manejador_niveles:
    def __init__(self,pantalla):
        self._slave = pantalla
        self.niveles={"nivel_uno": nivel_uno, "nivel_dos":nivel_dos_}


    def get_nivel(self, nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)