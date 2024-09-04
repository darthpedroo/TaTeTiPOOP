from fichas import Placeable
from exceptions import CasilleroOcupado

class Casillero():
    def __init__(self, columna, fila):
        self._columna = columna
        self._fila = fila
        self._symbol = "[-]"
        self._pieza = None

    @property
    def columna(self):
        return self._columna

    @property
    def fila(self):
        return self._fila

    @property
    def symbol(self):
        return self._symbol

    @property
    def pieza(self) -> Placeable | None:
        return self._pieza

    @pieza.setter
    def pieza(self, new_pieza: Placeable):
        if self._pieza != None:
            raise CasilleroOcupado()
        self._pieza = new_pieza

    def set_pieza_to_none(self):
        self._pieza = None

