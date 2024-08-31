from collections.abc import Iterable, Iterator
from abc import ABC
# pylint: disable=cSpell


class Placeable(ABC):
    def __init__(self):
        pass


class TaTeTiFicha(Placeable):
    def __init__(self):
        self._


class FichaCirculo(Placeable):
    def __init__(self):
        self._nombre = "Circulo"
        self._symbol = "O"  # HEREDAR ESTOOOOOO

    @property
    def symbol(self):
        return self._symbol


class FichaCuadrado(Placeable):
    def __init__(self):
        self._nombre = "Cuadrado"
        self._symbol = "[[]]"

    @property
    def symbol(self):
        return self._symbol


class Casillero():
    def __init__(self, columna, fila):
        self._columna = columna
        self._fila = fila
        self._symbol = "[-]"
        self._pieza = None

    @property
    def symbol(self):
        return self._symbol

    @property
    def pieza(self):
        return self._pieza

    @pieza.setter
    def pieza(self, new_pieza):
        self._pieza = new_pieza

    @pieza.setter
    def ficha(self, new_pieza):
        self._pieza = new_pieza


class Tablero(Iterable):
    def __init__(self, columnas, filas) -> None:
        self._columnas = columnas
        self._filas = filas
        self._tablero_matriz = self.crear_tablero()

    def __iter__(self):
        "Itera el tablero devolviendo por filas"
        for fila in range(self._filas):
            row_representation = []
            for columna in range(self._columnas):
                casillero = self._tablero_matriz[fila][columna]
                if casillero.pieza is None:
                    row_representation.append(casillero.symbol)
                else:
                    row_representation.append(casillero.pieza.symbol)

            yield "".join(row_representation)

    def crear_tablero(self):
        matriz = []
        for fila in range(self._filas):
            matriz.append([])
            for columna in range(self._columnas):
                new_tile = Casillero(columna, fila)
                matriz[fila].append(new_tile)

        matriz[0][0].pieza = FichaCuadrado()
        return matriz
