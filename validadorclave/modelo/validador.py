# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod

from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, \
    NoTieneLetraMinusculaError, NoTieneNumeroError, NoTieneCaracterEspecialError, NoTienePalabraSecretaError


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave: str):
        return any(letra.isupper() for letra in clave)

    def _contiene_minuscula(self, clave: str):
        return any(letra.islower() for letra in clave)

    def _contiene_numero(self, clave: str):
        return any(letra.isdigit() for letra in clave)

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        ...


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=8)

    def contiene_caracter_especial(self, clave: str):
        return any(letra in '@_#$%' for letra in clave)

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La clave debe tener una longitud de más de 8 caracteres.")
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError("La clave no contiene mayúsculas.")
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError('La clave no contiene minúsculas.')
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError('La clave no contiene números.')
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError('La clave no contiene un caracter especial.')
        return True


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=6)

    def contiene_calisto(self, clave: str) -> bool:
        palabra = 'calisto'
        clave_temp = clave.lower()
        index_calisto = 0

        while (index_calisto + len(palabra)) <= len(clave):
            index_calisto = clave_temp.find(palabra, index_calisto)

            if index_calisto >= 0:
                pi = index_calisto
                pf = index_calisto + len(palabra)
                palabra_original = clave[pi:pf]
                mayusculas = 0

                for letra in palabra_original:
                    if letra.isupper():
                        mayusculas += 1

                if 2 <= mayusculas < len(palabra):
                    return True
                else:
                    index_calisto = index_calisto + len(palabra)
            else:
                return False
        return False

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError('La clave no cumple con la longitud mínima.')
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError('La clave debe tener al menos un numero')
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError('La palabra calisto debe estar escrita con al menos dos letras en mayúscula')
        return True


class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla: ReglaValidacion = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)