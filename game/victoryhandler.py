from abc import ABC
from game.tablero import Tablero, Coordenadas
from game.team import TeamTaTeTi


class VictoryHandler(ABC):
    pass


class TaTeTiVictoryHandler(VictoryHandler):
    # Hacer que teams sea un args
    def __init__(self, points_to_win: int):
        self._points_to_win = points_to_win
        self._current_points = 0
        self._current_winner = None

    def decide_if_set_current_winner(self, casillero_coordenadas: Coordenadas, tablero: Tablero):
        casillero = tablero.get_specific_casillero_from_coordenadas(
            casillero_coordenadas)
        pieza = casillero.pieza
        if pieza is None:
            # Si no hay pieza reseteo el contador
            self._current_points = 0
            self._current_winner = None
        elif pieza == self._current_winner:
            self._current_points += 1
        else:
            self._current_winner = pieza  # Es nueva la secuencia, la empiezo acá
            self._current_points = 1
        return pieza

    def check_column(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero):
        for col in range(tablero.columnas):
            # Reseteo al ganador al cambiar de columna
            self._current_points = 0
            self._current_winner = None
            for row in range(tablero.filas):
                casillero_coordenadas = Coordenadas(col, row)
                self.decide_if_set_current_winner(
                    casillero_coordenadas, tablero)
                if self._current_points >= self._points_to_win:
                    return self.get_team_based_on_piece(list_of_teams, self._current_winner)

    def check_row(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero):

        for row in range(tablero.filas):
            self._current_points = 0
            self._current_winner = None
            for col in range(tablero.columnas):
                casillero_coordenadas = Coordenadas(col, row)
                self.decide_if_set_current_winner(
                    casillero_coordenadas, tablero)
                if self._current_points >= self._points_to_win:
                    return self.get_team_based_on_piece(list_of_teams, self._current_winner)

    def check_left_diagonal(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero):
        for row in range(tablero.filas):
            self._current_points = 0
            self._current_winner = None
            for column in range(tablero.columnas):
                # Pongo min porque si el tablero no es de dimension n*n tiene que agarrar el lado mas chico así no tira Error de index
                x_shift = column
                y_shift = row
                minimun_iteration_over_diagonal = min(
                    tablero.columnas - x_shift, tablero.filas - y_shift)
                for diagonal_iterator in range(minimun_iteration_over_diagonal):
                    diagonal_iterator_x = diagonal_iterator + x_shift
                    diagonal_iterator_y = diagonal_iterator + y_shift
                    casillero_coordenadas = Coordenadas(
                        diagonal_iterator_x, diagonal_iterator_y)
                    self.decide_if_set_current_winner(
                        casillero_coordenadas, tablero)
                if self._current_points >= self._points_to_win:
                    return self.get_team_based_on_piece(list_of_teams, self._current_winner)

    def check_right_diagonal(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero):
        for row in range(tablero.filas):
            self._current_points = 0
            self._current_winner = None
            for column in range(tablero.columnas):
                # For right diagonals, we start from (column, row) and move up-right
                x_shift = column
                y_shift = row
                # Determine the maximum number of steps we can take in the diagonal direction
                minimun_iteration_over_diagonal = min(
                    x_shift + 1, tablero.filas - y_shift)

                for diagonal_iterator in range(minimun_iteration_over_diagonal):
                    diagonal_iterator_x = x_shift - diagonal_iterator
                    diagonal_iterator_y = y_shift + diagonal_iterator
                    casillero_coordenadas = Coordenadas(
                        diagonal_iterator_x, diagonal_iterator_y)
                    self.decide_if_set_current_winner(
                        casillero_coordenadas, tablero)
                    if self._current_points >= self._points_to_win:
                        return self.get_team_based_on_piece(list_of_teams, self._current_winner)

    def check_empate(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero):
        if tablero.is_tablero_lleno():
            return list_of_teams

    def get_team_based_on_piece(self, list_of_teams: list[TeamTaTeTi], pieza):
        for team in list_of_teams:
            if team.pieza_del_equipo == pieza:
                return team

    # pasar el tablero aca, NO EN EL INIT
    def check_victory(self, list_of_teams: list[TeamTaTeTi], tablero: Tablero):
        column_win = self.check_column(list_of_teams, tablero)
        if column_win is not None:
            print("Ganador por columna: ", column_win)
            return column_win
        row_win = self.check_row(list_of_teams, tablero)
        if row_win is not None:
            print("Ganador por Fila: ", row_win)
            return row_win
        left_diagonal_win = self.check_left_diagonal(list_of_teams, tablero)
        if left_diagonal_win is not None:
            print("Ganador por Diagonal Izquierda: ", left_diagonal_win)
            return left_diagonal_win
        right_diagonal_win = self.check_right_diagonal(list_of_teams, tablero)
        if right_diagonal_win is not None:
            print("Ganador por Diagonal Derecha: ",
                  right_diagonal_win, tablero)
            return right_diagonal_win
        empate = self.check_empate(list_of_teams, tablero)
        if empate:
            print("Empate entre los equipos:", empate)
            return empate
        return None
