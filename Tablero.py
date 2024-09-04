from collections.abc import Iterable
from fichas import Placeable
from fichas import Placeable
from coordenadas import Coordenadas
from casillero import Casillero
from exceptions import CoordenadasFueraDelTablero, CasilleroOcupado

class Tablero(Iterable):
    def __init__(self, columnas, filas) -> None:
        self._columnas = columnas
        self._filas = filas
        self._tablero_matriz = self.crear_tablero()

    @property
    def tablero_matriz(self):
        return self._tablero_matriz

    @property
    def columnas(self):
        return self._columnas

    @property
    def filas(self):
        return self._filas

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
        if coordenadas.x > self._columnas or coordenadas.y > self._filas:
            raise CoordenadasFueraDelTablero()

        # IMPORTANTE. CODE SMELL!!!!!! FIJARSE PQ ESTA AL REVES :v. puede que sea el iterador :V
        return self._tablero_matriz[coordenadas.y][coordenadas.x]

    def agregar_pieza_a_casillero_from_coordenadas(self, coordenadas: Coordenadas, pieza: Placeable):
        casillero = self.get_specific_casillero_from_coordenadas(coordenadas)
        casillero.pieza = pieza

    def borrar_pieza_a_casillero_from_coordenadas(self, coordenadas: Coordenadas):
        casillero = self.get_specific_casillero_from_coordenadas(coordenadas)
        casillero.set_pieza_to_none()

    def is_tablero_lleno(self):
        for columna in range(self._columnas):
            for fila in range(self._filas):
                coordenadas_pieza = Coordenadas(columna,fila)
                if self.get_specific_casillero_from_coordenadas(coordenadas_pieza).pieza is None:
                    return False
        return True 
