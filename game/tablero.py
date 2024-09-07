from collections.abc import Iterable
from game.fichas import Placeable
from game.coordenadas import Coordenadas
from game.casillero import Casillero
from game.exceptions import CoordenadasFueraDelTablero, CasilleroOcupado, CoordenadasNoSonPositivas


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

    def check_if_coordenadas_fuera_del_tablero(self, coordenadas: Coordenadas):
        if coordenadas.x > self._columnas-1 or coordenadas.y > self._filas-1:
            raise CoordenadasFueraDelTablero()

    def get_specific_casillero_from_coordenadas(self, coordenadas: Coordenadas) -> Casillero:
        """Devuelve un casillero del tablero en base a coordenadas específicas
        Args:
            coordenadas (Coordenadas):

        Returns:
            Casillero: (Casillero)
        """
        self.check_if_coordenadas_fuera_del_tablero(coordenadas)

        # IMPORTANTE. CODE SMELL!!!!!! FIJARSE PQ ESTA AL REVES :v. puede que sea el iterador :V
        return self._tablero_matriz[coordenadas.y][coordenadas.x]

    def get_casillero_neighbour_exception_handler(self, casillero: Casillero, fila_index: int, columna_modifier: int):
        try:
            coordenadas_up_neighbour = Coordenadas(  # HACER QUE ESE 0 SEA EL PARAMETRO X SI SE NECESITA EL UP_DOWN_LEFT_RIGHT_ETC......
                casillero.columna + columna_modifier, casillero.fila+fila_index)  # OJO CON ESTE, MODIFICARLO EN LA IMPLEMENTACION
            return self.get_specific_casillero_from_coordenadas(coordenadas_up_neighbour)
        except CoordenadasFueraDelTablero:
            return None
        except CoordenadasNoSonPositivas:
            return None

    def get_casillero_up_neighbour(self, casillero: Casillero, fila_index: int):
        return self.get_casillero_neighbour_exception_handler(casillero, -fila_index, 0)

    def get_casillero_down_neighbour(self, casillero: Casillero, fila_index: int):
        return self.get_casillero_neighbour_exception_handler(casillero, +fila_index, 0)

    # TESTEAR ESTE
    def get_casillero_left_neighbour(self, casillero: Casillero, columna_index: int):
        return self.get_casillero_neighbour_exception_handler(casillero, 0, -columna_index)

        coordenadas_left_neighbour = Coordenadas(
            casillero.columna - 1, casillero.fila)  # IMPLEMENTAR ESTO EN EL get_casillero_neighbour_exception_handler. H
        return self.get_specific_casillero_from_coordenadas(coordenadas_left_neighbour)

    def get_casillero_right_neighbour(self, casillero: Casillero):
        coordenadas_right_neighbour = Coordenadas(
            casillero.columna + 1, casillero.fila)
        return self.get_specific_casillero_from_coordenadas(coordenadas_right_neighbour)

    def agregar_pieza_a_casillero_from_coordenadas(self, coordenadas: Coordenadas, pieza: Placeable):
        casillero = self.get_specific_casillero_from_coordenadas(coordenadas)
        casillero.pieza = pieza

    def borrar_pieza_a_casillero_from_coordenadas(self, coordenadas: Coordenadas):
        casillero = self.get_specific_casillero_from_coordenadas(coordenadas)
        casillero.set_pieza_to_none()

    def is_tablero_lleno(self):
        for columna in range(self._columnas):
            for fila in range(self._filas):
                coordenadas_pieza = Coordenadas(columna, fila)
                if self.get_specific_casillero_from_coordenadas(coordenadas_pieza).pieza is None:
                    return False
        return True

    def volver_a_crear_tablero(self):
        self._tablero_matriz = self.crear_tablero()
