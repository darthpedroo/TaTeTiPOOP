from abc import ABC
from game.tablero import Tablero, Coordenadas
from game.team import TeamTaTeTi
from game.casillero import Casillero


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

    def points_adder(self, last_casillero: Casillero, fila: int, funcion):
        casillero = funcion(last_casillero, fila)
        if casillero is None:
            return False
        elif casillero.pieza == last_casillero.pieza:
            self._current_points += 1
        elif casillero.pieza is not None and casillero.pieza != last_casillero.pieza:
            return False
        return True

    def strategy_checker(self, list_of_teams: list[TeamTaTeTi], last_casillero: Casillero, first_checker_function, second_checker_function):
        checking = True
        fila = 0
        while checking:
            checking = self.points_adder(
                last_casillero, fila, first_checker_function)
            fila += 1

        checking = True
        fila = 0
        while checking:
            checking = self.points_adder(
                last_casillero, fila, second_checker_function)
            fila += 1

        if self._current_points >= self._points_to_win:
            return self.get_team_based_on_piece(list_of_teams, last_casillero.pieza)
        self._current_points = 0
        return None

    def check_column(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero, last_casillero: Casillero):
        return self.strategy_checker(list_of_teams, last_casillero, tablero.get_casillero_up_neighbour,
                                     tablero.get_casillero_down_neighbour)

    def check_row(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero, last_casillero: Casillero):
        return self.strategy_checker(list_of_teams, last_casillero, tablero.get_casillero_left_neighbour,
                                     tablero.get_casillero_right_neighbour)

    def check_victory(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero, last_casillero: Casillero):
        return self.check_column(list_of_teams, tablero, last_casillero)
