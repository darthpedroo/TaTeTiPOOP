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

    def check_column(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero, last_casillero: Casillero):

        rango_check_down = (tablero.filas-1)-last_casillero.fila
        rango_check_up = last_casillero.fila
        for fila in range(rango_check_down):  # Para iterar para abajo
            casillero = tablero.get_casillero_down_neighbour(last_casillero)
            if casillero.pieza == last_casillero.pieza:
                self._current_points += 1
        for fila in range(rango_check_up):  # Para iterar para arriba
            casillero = tablero.get_casillero_up_neighbour(last_casillero)
            if casillero.pieza == last_casillero.pieza:
                self._current_points += 1

        if self._current_points >= self._points_to_win:
            return self.get_team_based_on_piece(list_of_teams, last_casillero.pieza)
        self._current_points = 0

    def check_victory(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero, last_casillero: Casillero):

        self.check_column(list_of_teams, tablero, last_casillero)
