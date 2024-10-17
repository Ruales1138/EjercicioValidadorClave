# TODO: Implementa el código del ejercicio aquí

from abc import ABC, abstractmethod


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    @abstractmethod
    def es_valida(self, clave):
        pass

    def _validar_longitud(self, clave):
        return len(clave) > self._longitud_esperada

class ReglaLongitud(ReglaValidacion):
    def __init__(self, longitud_esperada):
        super().__init__(longitud_esperada)

    def es_valida(self, clave):
        return self._validar_longitud(clave)

    def _contiene_mayuscula(self):
        pass



class Validador():
    pass


class ReglaValidacionGanimedes():
    pass


class ReglaValidacionCalisto():
    pass