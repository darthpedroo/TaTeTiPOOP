from abc import ABC
from game.tablero import Tablero, Coordenadas
from game.team import TeamTaTeTi
from game.casillero import Casillero
from typing import Callable


class VictoryHandler(ABC):
    pass


class TaTeTiVictoryHandler(VictoryHandler):
    # Hacer que teams sea un args
    def __init__(self, points_to_win: int):
        self._points_to_win = points_to_win - 1
        self._current_points = 0

    def get_team_based_on_piece(self, list_of_teams: list[TeamTaTeTi], pieza):
        for team in list_of_teams:
            if team.pieza_del_equipo == pieza:
                return team

    def points_adder(self, last_casillero: Casillero, fila: int, columna: int, funcion):
        casillero = funcion(last_casillero, fila, columna)
        if casillero is None:
            return False
        elif casillero.pieza == last_casillero.pieza:
            self._current_points += 1
        elif casillero.pieza is not None and casillero.pieza != last_casillero.pieza:
            return False
        return True

    def checker_for_points_adder(self, last_casillero: Casillero, checker_function: Callable, fila_adder: bool, column_adder: bool):
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

    def strategy_checker(self, list_of_teams: list[TeamTaTeTi], last_casillero: Casillero, fila_adder: bool, column_adder: bool, first_checker_function: Callable, second_checker_function: Callable):

        self.checker_for_points_adder(last_casillero, first_checker_function,
                                      fila_adder, column_adder)
        self.checker_for_points_adder(last_casillero, second_checker_function,
                                      fila_adder, column_adder)

        if self._current_points >= self._points_to_win:
            return self.get_team_based_on_piece(list_of_teams, last_casillero.pieza)
        self._current_points = 0
        return None

    def check_column(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero, last_casillero: Casillero):
        return self.strategy_checker(list_of_teams, last_casillero, True, False, tablero.get_casillero_up_neighbour,
                                     tablero.get_casillero_down_neighbour)

    def check_row(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero, last_casillero: Casillero):
        return self.strategy_checker(list_of_teams, last_casillero, False, True, tablero.get_casillero_left_neighbour,
                                     tablero.get_casillero_right_neighbour)

    def check_left_diagonal(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero, last_casillero: Casillero):
        return self.strategy_checker(list_of_teams, last_casillero, True, True, tablero.get_casillero_down_left_neighbour, tablero.get_casillero_top_right_neighbour)

    def check_right_diagonal(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero, last_casillero: Casillero):
        return self.strategy_checker(list_of_teams, last_casillero, True, True, tablero.get_casillero_top_left_neighbour, tablero.get_casillero_down_right_neighbour)

    def check_empate(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero):
        if tablero.is_tablero_lleno():
            return list_of_teams

    def check_victory(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero, last_casillero: Casillero):
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
