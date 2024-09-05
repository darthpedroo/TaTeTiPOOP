from abc import ABC


class Placeable(ABC):
    def __init__(self):
        pass


class TaTeTiFicha(Placeable):
    def __init__(self, nombre, symbol):
        self._nombre = nombre
        self._symbol = symbol

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


class FichaCirculo(TaTeTiFicha):
    def __init__(self):
        super().__init__(nombre="Circulo", symbol="[O]")


class FichaCuadrado(TaTeTiFicha):
    def __init__(self):
        super().__init__(nombre="Cuadrado", symbol="[[]]")

class FichaCruz(TaTeTiFicha):
    def __init__(self):
        super().__init__(nombre="Cruz", symbol="[X]")


    