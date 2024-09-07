from game.fichas import Placeable
from game.exceptions import CasilleroOcupado


class Casillero():
    """
    Representa un casillero del Tablero
    Attributes:
        columna (int)
        fila (int)
        symbol (str)
        pieza (Placeable | None)
    """

    def __init__(self, columna, fila):
        self._columna = columna
        self._fila = fila
        self._symbol = "[-]"
        self._pieza = None  # Hacer un metodo "CasilleroOcupado y que devuelva true or false y dps"

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
