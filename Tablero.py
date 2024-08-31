from collections.abc import Iterable
from abc import ABC
from fichas import FichaCirculo, FichaCuadrado, FichaCruz, Placeable


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
        self._pieza = new_pieza

    def set_pieza_to_none(self):
        self._pieza = None


class Coordenadas():
    """Clase que representa coordenadas en el tablero.

    Attributes:
        x (int): La posición en la columna del tablero (eje X).
        y (int): La posición en la fila del tablero (eje Y).
    """

    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


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
        return matriz

    def get_specific_casillero_from_coordenadas(self, coordenadas: Coordenadas) -> Casillero:
        """Devuelve un casillero del tablero en base a coordenadas específicas

        Args:
            coordenadas (Coordenadas):

        Returns:
            Casillero: (Casillero)
        """
        return self._tablero_matriz[coordenadas.x][coordenadas.y]

    def agregar_pieza_a_casillero_from_coordenadas(self, coordenadas: Coordenadas, pieza: Placeable):
        casillero = self.get_specific_casillero_from_coordenadas(coordenadas)
        casillero.pieza = pieza

    def borrar_pieza_a_casillero_from_coordenadas(self, coordenadas: Coordenadas):
        casillero = self.get_specific_casillero_from_coordenadas(coordenadas)
        casillero.set_pieza_to_none()
