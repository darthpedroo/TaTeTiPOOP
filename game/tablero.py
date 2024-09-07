from collections.abc import Iterable
from game.fichas import Placeable
from game.coordenadas import Coordenadas
from game.casillero import Casillero
from game.exceptions import CoordenadasFueraDelTablero, CasilleroOcupado, CoordenadasNoSonPositivas


class Tablero(Iterable):

    """Clase que representa el Tablero.

    Attributes:
        columnas (int): La cantidad de columnas que tiene el tablero.
        filas (int): La cantidad de filas que tiene el tablero.
        tablero_matriz (list[list]): La representacion del tablero como una matriz de listas con listas.
    """

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
        """Crea una matriz NxN de Casilleros que representa el tablero.

        Returns:
            list[list[Casillero]]: La matriz de casilleros del tablero.
        """
        matriz = []
        for fila in range(self._filas):
            matriz.append([])
            for columna in range(self._columnas):
                new_tile = Casillero(columna, fila)
                matriz[fila].append(new_tile)
        return matriz

    def check_if_coordenadas_fuera_del_tablero(self, coordenadas: Coordenadas):
        """Checkea si las coordenadas están fuera del tablero y tira una excepción si están afuera del tablero.

        Args:
            coordenadas (Coordenadas): Las coordenadas a verificar.

        Raises:
            CoordenadasFueraDelTablero: Si las coordenadas están fuera del tablero.
        """
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
        """Función que facilita y sistemiza la forma de obtener casilleros vecinos

        Args:
            casillero (Casillero): El casillero central.
            fila_index (int): La fila de cambio para acceder al neighbour.
            columna_modifier (int): La columna de cambio para acceder al neighbour.

        Returns:
            Casillero | None: Si tiene casillero vecino, lo devuelve. Si se hace un catch de una excepción, devuelve None
        """
        try:
            coordenadas_up_neighbour = Coordenadas(
                casillero.columna + columna_modifier, casillero.fila+fila_index)
            return self.get_specific_casillero_from_coordenadas(coordenadas_up_neighbour)
        except CoordenadasFueraDelTablero:
            return None
        except CoordenadasNoSonPositivas:
            return None

    def get_casillero_up_neighbour(self, casillero: Casillero, fila_index: int, columa_index: int):
        """Obtiene el casillero de arriba de un casillero específico

        Args:
            casillero (Casillero): El casillero central.
            fila_index (int): La fila de cambio para acceder al neighbour.
            columa_index (int): La columna de cambio para acceder al neighbour.

        Returns:
            Casillero | None: Si tieen casillero vecino, lo devuelve, sino devuelve None
        """
        return self.get_casillero_neighbour_exception_handler(casillero, -fila_index, columa_index)

    def get_casillero_down_neighbour(self, casillero: Casillero, fila_index: int, columa_index: int):
        """Obtiene el casillero de abajo de un casillero específico

        Args:
            casillero (Casillero): El casillero central.
            fila_index (int): La fila de cambio para acceder al neighbour.
            columa_index (int): La columna de cambio para acceder al neighbour.

        Returns:
            Casillero | None: Si tieen casillero vecino, lo devuelve, sino devuelve None
        """
        return self.get_casillero_neighbour_exception_handler(casillero, +fila_index, columa_index)

    def get_casillero_left_neighbour(self, casillero: Casillero,  fila_index: int, columna_index: int):
        """Obtiene el casillero de la izquierda de un casillero específico

        Args:
            casillero (Casillero): El casillero central.
            fila_index (int): La fila de cambio para acceder al neighbour.
            columa_index (int): La columna de cambio para acceder al neighbour.

        Returns:
            Casillero | None: Si tieen casillero vecino, lo devuelve, sino devuelve None
        """
        return self.get_casillero_neighbour_exception_handler(casillero, fila_index, -columna_index)

    def get_casillero_right_neighbour(self, casillero: Casillero, fila_index: int, columna_index: int):
        """Obtiene el casillero de la derecha de un casillero específico

        Args:
            casillero (Casillero): El casillero central.
            fila_index (int): La fila de cambio para acceder al neighbour.
            columa_index (int): La columna de cambio para acceder al neighbour.

        Returns:
            Casillero | None: Si tieen casillero vecino, lo devuelve, sino devuelve None
        """
        return self.get_casillero_neighbour_exception_handler(casillero, fila_index, +columna_index)

    def get_casillero_top_left_neighbour(self, casillero: Casillero, fila_index: int, columna_index: int):
        """Obtiene el casillero de arriba a la izquierda de un casillero específico

        Args:
            casillero (Casillero): El casillero central.
            fila_index (int): La fila de cambio para acceder al neighbour.
            columa_index (int): La columna de cambio para acceder al neighbour.

        Returns:
            Casillero | None: Si tieen casillero vecino, lo devuelve, sino devuelve None
        """
        return self.get_casillero_neighbour_exception_handler(casillero, -fila_index, - columna_index)

    def get_casillero_down_right_neighbour(self, casillero: Casillero, fila_index: int, columna_index: int):
        """Obtiene el casillero de abajo a la derecha de un casillero específico

        Args:
            casillero (Casillero): El casillero central.
            fila_index (int): La fila de cambio para acceder al neighbour.
            columa_index (int): La columna de cambio para acceder al neighbour.

        Returns:
            Casillero | None: Si tieen casillero vecino, lo devuelve, sino devuelve None
        """
        return self.get_casillero_neighbour_exception_handler(casillero, +fila_index, + columna_index)

    def get_casillero_down_left_neighbour(self, casillero: Casillero, fila_index: int, columna_index: int):
        """Obtiene el casillero de abajo a la izquierda de un casillero específico

        Args:
            casillero (Casillero): El casillero central.
            fila_index (int): La fila de cambio para acceder al neighbour.
            columa_index (int): La columna de cambio para acceder al neighbour.

        Returns:
            Casillero | None: Si tieen casillero vecino, lo devuelve, sino devuelve None
        """
        return self.get_casillero_neighbour_exception_handler(casillero, +fila_index, - columna_index)

    def get_casillero_top_right_neighbour(self, casillero: Casillero, fila_index: int, columna_index: int):
        """Obtiene el casillero de arriba a la derecha de un casillero específico

        Args:
            casillero (Casillero): El casillero central.
            fila_index (int): La fila de cambio para acceder al neighbour.
            columa_index (int): La columna de cambio para acceder al neighbour.

        Returns:
            Casillero | None: Si tieen casillero vecino, lo devuelve, sino devuelve None
        """
        return self.get_casillero_neighbour_exception_handler(casillero, -fila_index, + columna_index)

    def agregar_pieza_a_casillero_from_coordenadas(self, coordenadas: Coordenadas, pieza: Placeable):
        """Agrega pieza a casillero según coordenadas específicas.

        Args:
            coordenadas (Coordenadas): Las coordenadas del casilllero donde se va a agregar la pieza.
            pieza (Placeable): La pieza a colocar en el tablero.
        """
        casillero = self.get_specific_casillero_from_coordenadas(coordenadas)
        casillero.pieza = pieza

    def borrar_pieza_a_casillero_from_coordenadas(self, coordenadas: Coordenadas):
        """Elimina pieza a casillero según coordenadas específicas.

        Args:
            coordenadas (Coordenadas): Las coordenadas del casilllero donde se va a borrar la pieza.
        """
        casillero = self.get_specific_casillero_from_coordenadas(coordenadas)
        casillero.set_pieza_to_none()

    def is_tablero_lleno(self):
        """Verifica si el tablero está lleno (una pieza en todos los casilleros)

        Returns:
            bool: True si el tablero está lleno False si no está lleno.
        """
        for columna in range(self._columnas):
            for fila in range(self._filas):
                coordenadas_pieza = Coordenadas(columna, fila)
                if self.get_specific_casillero_from_coordenadas(coordenadas_pieza).pieza is None:
                    return False
        return True

    def volver_a_crear_tablero(self):
        """Vuelve a generar la matriz del tablero según las dimensiones NxN proporcionadas en el __init__"""
        self._tablero_matriz = self.crear_tablero()
