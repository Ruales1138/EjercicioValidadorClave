# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod

from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, \
    NoTieneLetraMinusculaError, NoTieneNumeroError, NoTieneCaracterEspecialError, NoTienePalabraSecretaError


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave: str) -> bool:
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave: str) -> bool:
        return any(c.isdigit() for c in clave)

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        pass

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La clave no cumple con la longitud mínima.")
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError("La clave no contiene mayúsculas.")
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError("La clave no contiene minúsculas.")
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave no contiene números.")
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError("La clave no contiene un caracter especial.")
        return True

class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=6)

    def contiene_calisto(self, clave: str) -> bool:
        pass

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La clave no cumple con la longitud mínima.")
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError("La clave no contiene 'calisto' con las mayúsculas requeridas.")
        return True


class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)