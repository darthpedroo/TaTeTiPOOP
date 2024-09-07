from abc import ABC
from game.tablero import Tablero
from game.team import TeamTaTeTi
from game.casillero import Casillero
from game.fichas import Placeable
from typing import Callable


class VictoryHandler(ABC):
    """Clase abstacta de VictoryHandler como base para las distintas implementaciones de las victorias que puede tener un juego"""
    pass


class TaTeTiVictoryHandler(VictoryHandler):
    """Handler de la victoria tradicional del TaTeTi, soporte para tablero dinámico

    Args: 
        points_to_win (int): La cantidad de puntos necesarios para ganar
        current_points (int): La cantidad de puntos actuales.

    """

    def __init__(self, points_to_win: int):
        self._points_to_win = points_to_win - 1
        self._current_points = 0

    def get_team_based_on_piece(self, list_of_teams: list[TeamTaTeTi], pieza: Placeable) -> TeamTaTeTi:
        """Obtiene un equipo segpun la pieza seleccionada

        Args:
            list_of_teams (list[TeamTaTeTi]): Lista de equipos para seleccionar la pieza
            pieza (Placeable): Pieza para filtrar los equipos

        Returns:
            TeamTaTeTi: Equipo que tiene la pieza filtrada
        """
        for team in list_of_teams:
            if team.pieza_del_equipo == pieza:
                return team

    def points_adder(self, last_casillero: Casillero, fila: int, columna: int, funcion: Callable) -> bool:
        """Suma puntos si el casillero actual es igual al último casillero.

        Args:
            last_casillero (Casillero): Casillero a comparar
            fila (int): fila de la iteracion para pasarle a la función checker
            columna (int): columna de la iteración para pasarle a la función checker
            funcion (Callable): La función que checkea si ganó, Ej: (check_row, check_column, check_diagonal)

        Returns:
            bool: Devuelve True si se puede seguir checkeando, devuelve False si no hay que checkear más.
        """
        casillero = funcion(last_casillero, fila, columna)
        if casillero is None:
            return False
        elif casillero.pieza == last_casillero.pieza:
            self._current_points += 1
        elif casillero.pieza is not None and casillero.pieza != last_casillero.pieza:
            return False
        return True

    def checker_for_points_adder(self, last_casillero: Casillero, checker_function: Callable, fila_adder: bool, column_adder: bool):
        """Checker que repite la función points_adder hasta que se termine de checkear una strategia de victoria específica

        Args:
            last_casillero (Casillero): Casillero a checkear
            checker_function (Callable): La función que checkea si ganó, Ej: (check_row, check_column, check_diagonal)
            fila_adder (bool): True si se quiere sumar a la fila, False si no
            column_adder (bool): True si se quiere sumar a la columna, False si no
        """
        checking = True
        fila = 0
        columna = 0
        while checking:
            if fila_adder:
                fila += 1
            if column_adder:
                columna += 1
            checking = self.points_adder(
                last_casillero, fila, columna, checker_function)

    def strategy_checker(self, list_of_teams: list[TeamTaTeTi], last_casillero: Casillero, fila_adder: bool, column_adder: bool, first_checker_function: Callable, second_checker_function: Callable) -> TeamTaTeTi | None:
        """Chceckea si hay un ganador segun estrategia especifica

        Args:
            list_of_teams (list[TeamTaTeTi]): lista de los equipos que se queire comparar la victoria
            last_casillero (Casillero): ultimo casillero a comparar 
            fila_adder (bool): True si se quiere sumar a la fila, False si no
            column_adder (bool): True si se quiere sumar a la columna, False si no
            first_checker_function (Callable):  La función que checkea si ganó, Ej: (check_row, check_column, check_diagonal)
            second_checker_function (Callable):  La función que checkea si ganó, Ej: (check_row, check_column, check_diagonal)

        Returns:
            TeamTaTeTi: Devuelve El team que gano | None: Devuelve que no ganó ningún team
        """

        self.checker_for_points_adder(last_casillero, first_checker_function,
                                      fila_adder, column_adder)
        self.checker_for_points_adder(last_casillero, second_checker_function,
                                      fila_adder, column_adder)

        if self._current_points >= self._points_to_win:
            return self.get_team_based_on_piece(list_of_teams, last_casillero.pieza)
        self._current_points = 0
        return None

    def check_column(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero, last_casillero: Casillero) -> TeamTaTeTi | None:
        """Checkea si se ganó mediante la columna

        Args:
            list_of_teams (list[TeamTaTeTi]): Lista de los equipos con los cuales checkear la victoria
            tablero (Tablero): Tablero para iterar y buscar los casilleros
            last_casillero (Casillero): Ultimo casillero donde se puso una pieza

        Returns:
            TeamTaTeTi: Devuelve El team que gano | None: Devuelve que no ganó ningún team
        """
        return self.strategy_checker(list_of_teams, last_casillero, True, False, tablero.get_casillero_up_neighbour,
                                     tablero.get_casillero_down_neighbour)

    def check_row(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero, last_casillero: Casillero):
        """Checkea si se ganó mediante la fila

        Args:
            list_of_teams (list[TeamTaTeTi]): Lista de los equipos con los cuales checkear la victoria
            tablero (Tablero): Tablero para iterar y buscar los casilleros
            last_casillero (Casillero): Ultimo casillero donde se puso una pieza

        Returns:
            TeamTaTeTi: Devuelve El team que gano | None: Devuelve que no ganó ningún team
        """
        return self.strategy_checker(list_of_teams, last_casillero, False, True, tablero.get_casillero_left_neighbour,
                                     tablero.get_casillero_right_neighbour)

    def check_left_diagonal(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero, last_casillero: Casillero):
        """Checkea si se ganó mediante la diagonal izquierda

        Args:
            list_of_teams (list[TeamTaTeTi]): Lista de los equipos con los cuales checkear la victoria
            tablero (Tablero): Tablero para iterar y buscar los casilleros
            last_casillero (Casillero): Ultimo casillero donde se puso una pieza

        Returns:
            TeamTaTeTi: Devuelve El team que gano | None: Devuelve que no ganó ningún team
        """
        return self.strategy_checker(list_of_teams, last_casillero, True, True, tablero.get_casillero_down_left_neighbour, tablero.get_casillero_top_right_neighbour)

    def check_right_diagonal(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero, last_casillero: Casillero):
        """Checkea si se ganó mediante la diagonal derecha

        Args:
            list_of_teams (list[TeamTaTeTi]): Lista de los equipos con los cuales checkear la victoria
            tablero (Tablero): Tablero para iterar y buscar los casilleros
            last_casillero (Casillero): Ultimo casillero donde se puso una pieza

        Returns:
            TeamTaTeTi: Devuelve El team que gano | None: Devuelve que no ganó ningún team
        """
        return self.strategy_checker(list_of_teams, last_casillero, True, True, tablero.get_casillero_top_left_neighbour, tablero.get_casillero_down_right_neighbour)

    def check_empate(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero) -> list[TeamTaTeTi] | None:
        """Checkea si se empató la partida

        Args:
            list_of_teams (list[TeamTaTeTi]): Lista de los equipos con los cuales checkear el empate
            tablero (Tablero): Tablero para iterar y buscar los casilleros

        Returns:
            list[TeamTaTeTi]: Devuelve los teams que empataron | None: Devuelve que no se empató 
        """
        if tablero.is_tablero_lleno():
            return list_of_teams
        return None

    def check_victory(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero, last_casillero: Casillero) -> TeamTaTeTi | list[TeamTaTeTi] | None:
        """Checkea las distintas formas de ganar y devulve un ganador o un empate

        Args:
            list_of_teams (list[TeamTaTeTi]): equipos contra los que checkear la victoria
            tablero (Tablero): Tablero para iterar y buscar los casilleros
            last_casillero (Casillero): Ultimo casillero donde se puso una pieza

        Returns:
            TeamTatei: Si ganó un equipo especifico
            list[TeamTatei]: Si hubo empate
            None: Si no gano ni empato nadie
        """
        check_column = self.check_column(
            list_of_teams, tablero, last_casillero)

        if check_column is not None:
            self._current_points = 0
            return check_column

        check_row = self.check_row(list_of_teams, tablero, last_casillero)
        if check_row is not None:
            self._current_points = 0
            return check_row
        check_left_diagonal = self.check_left_diagonal(
            list_of_teams, tablero, last_casillero)
        if check_left_diagonal is not None:
            self._current_points = 0
            return check_left_diagonal

        check_right_diagonal = self.check_right_diagonal(
            list_of_teams, tablero, last_casillero)

        if check_right_diagonal is not None:
            self._current_points = 0
            return check_right_diagonal
        empate = self.check_empate(list_of_teams, tablero)
        if empate:
            return empate
        return None
