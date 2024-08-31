from collections.abc import Iterable, Iterator
from abc import ABC
# pylint: disable=cSpell


class Placeable(ABC):
    def __init__(self):
        pass


class FichaCirculo(Placeable):
    def __init__(self):
        self._nombre = "Circulo"
        self._symbolo = "O"


class FichaCuadrado(Placeable):
    def __init__(self):
        self._nombre = "Circulo"
        self._symbolo = "O"


class Casillero():
    def __init__(self, columna, fila):
        self._columna = columna
        self._fila = fila
        self._symbol = "[X]"
        self._pieza = None

    @property
    def symbol(self):
        return self._symbol

    @property
    def pieza(self):
        return self._ficha

    @pieza.setter
    def ficha(self, new_ficha):
        self._ficha = new_ficha


class Tablero(Iterable):
    def __init__(self, columnas, filas) -> None:
        self._columnas = columnas
        self._filas = filas
        self._tablero_matriz = self.crear_tablero()

    def __iter__(self):
        "Itera el tablero devolviendo por filas"

        # si la pieza es null mostrar simbolo, sino la ficha
        for fila in range(self._filas):
            yield "".join(self._tablero_matriz[fila][columna].symbol for columna in range(self._columnas))

    def crear_tablero(self):
        matriz = []
        for fila in range(self._filas):
            matriz.append([])
            for columna in range(self._columnas):
                new_tile = Casillero(columna, fila)
                matriz[fila].append(new_tile)
        return matriz
