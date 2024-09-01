from abc import ABC
from tablero import Tablero
from fichas import FichaCirculo, FichaCruz, FichaCuadrado
from team import TeamTaTeTi


class VictoryHandler(ABC):
    pass


class TaTeTiVictoryHandler(VictoryHandler):
    # Hacer que teams sea un args
    def __init__(self, points_to_win: int, tablero: Tablero | None = None, list_of_teams: list[TeamTaTeTi] | None = None):
        self._tablero_to_check_victory = tablero
        self._list_of_teams = list_of_teams
        self._points_to_win = points_to_win

    @property
    def tablero_to_check_victory(self):
        return self._tablero_to_check_victory

    @tablero_to_check_victory.setter
    def tablero_to_check_victory(self, new_tablero: Tablero):
        self._tablero_to_check_victory = new_tablero

    @property
    def list_of_teams(self):
        return self._tablero_to_check_victory

    @list_of_teams.setter
    def list_of_teams(self, new_list_of_teams: list[TeamTaTeTi]):
        self._list_of_teams = new_list_of_teams

    # Hay 8 posibles combinaciones para ganar

    def get_list_of_pieces_from_team(self):
        list_of_pieces = []

        for team in self._list_of_teams:
            list_of_pieces.append(team.pieza_del_equipo)
        return list_of_pieces

    def check_column(self):
        for col in range(self.tablero_to_check_victory.columnas):
            # Reseteo al ganador al cambiar de columna
            current_winner = None
            current_points = 0
            for row in range(self.tablero_to_check_victory.filas):
                pieza = self.tablero_to_check_victory.tablero_matriz[row][col].pieza
                if pieza is None:
                    # Si no hay pieza reseteo el contador
                    current_points = 0
                    current_winner = None
                elif pieza == current_winner:
                    current_points += 1
                else:
                    current_winner = pieza  # Es nueva la secuencia, la empiezo acá
                    current_points = 1
                if current_points >= self._points_to_win:
                    return current_winner

    def check_row(self):
        for row in range(self.tablero_to_check_victory.filas):
            current_winner = None
            current_points = 0
            for col in range(self.tablero_to_check_victory.columnas):
                pieza = self.tablero_to_check_victory.tablero_matriz[row][col].pieza
                if pieza is None:
                    current_points = 0
                    current_winner = None
                elif pieza == current_winner:
                    current_points += 1
                else:
                    current_winner = pieza
                    current_points = 1

                if current_points >= self._points_to_win:
                    return current_winner

    def check_victory(self):

        column_win = self.check_column()
        row_win = self.check_row()

        if column_win is not None:
            return column_win
        if row_win is not None:
            return row_win

        return None
