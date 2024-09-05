from abc import ABC


class Placeable(ABC):
    def __init__(self):
        pass


class TaTeTiFicha(Placeable):
    def __init__(self, nombre, symbol, identificador):
        self._nombre = nombre
        self._symbol = symbol
        self._identificador = identificador

    def __eq__(self, other: 'TaTeTiFicha') -> bool:
        if other is None:
            return False
        if self._symbol == other._symbol:
            return True
        return False

    @property
    def nombre(self):
        return self._nombre

    @property
    def symbol(self):
        return self._symbol

    @property
    def identificador(self):
        return self._identificador


class FichaCirculo(TaTeTiFicha):
    def __init__(self):
        super().__init__(nombre="Circulo", symbol="[O]", identificador="O")


class FichaSigma(TaTeTiFicha):
    def __init__(self):
        super().__init__(nombre="SigmaFace", symbol="[🗿]", identificador="S")


class FichaCruz(TaTeTiFicha):
    def __init__(self):
        super().__init__(nombre="Cruz", symbol="[X]", identificador="X")


class FichaVater(TaTeTiFicha):
    def __init__(self):
        super().__init__(nombre="Vater", symbol="[🚽]", identificador="V")
