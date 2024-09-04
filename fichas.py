from abc import ABC


class Placeable(ABC):
    def __init__(self):
        pass


class TaTeTiFicha(Placeable):
    def __init__(self, nombre, symbol):
        self._nombre = nombre
        self._symbol = symbol

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


    