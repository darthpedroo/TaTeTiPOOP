from abc import ABC
from tablero import Tablero, Coordenadas
from fichas import FichaCirculo, FichaCruz, FichaCuadrado
from team import TeamTaTeTi


class VictoryHandler(ABC):
    pass


class TaTeTiVictoryHandler(VictoryHandler):
    # Hacer que teams sea un args
    def __init__(self, points_to_win: int, tablero: Tablero | None = None):
        self._tablero_to_check_victory = tablero
        self._points_to_win = points_to_win
        self._current_points = 0
        self._current_winner = None

    @property
    def tablero_to_check_victory(self):
        return self._tablero_to_check_victory

    @tablero_to_check_victory.setter
    def tablero_to_check_victory(self, new_tablero: Tablero):
        self._tablero_to_check_victory = new_tablero



    def decide_if_set_current_winner(self, casillero_coordenadas : Coordenadas):
        casillero = self.tablero_to_check_victory.get_specific_casillero_from_coordenadas(
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


    def check_column(self,list_of_teams: list[TeamTaTeTi]):
        for col in range(self.tablero_to_check_victory.columnas):
            # Reseteo al ganador al cambiar de columna
            self._current_points = 0 
            self._current_winner = None
            for row in range(self.tablero_to_check_victory.filas):
                casillero_coordenadas = Coordenadas(col, row)
                self.decide_if_set_current_winner(casillero_coordenadas)
                if self._current_points >= self._points_to_win:
                    return self._current_winner

    def check_row(self,list_of_teams: list[TeamTaTeTi]):
        for row in range(self.tablero_to_check_victory.filas):
            self._current_points = 0 
            self._current_winner = None
            for col in range(self.tablero_to_check_victory.columnas):
                casillero_coordenadas = Coordenadas(col, row)
                self.decide_if_set_current_winner(casillero_coordenadas)
                if self._current_points >= self._points_to_win:
                    return self._current_winner

    def check_left_diagonal(self, list_of_teams: list[TeamTaTeTi]):
        for row in range(self.tablero_to_check_victory.filas):
            self._current_points = 0 
            self._current_winner = None
            for column in range(self.tablero_to_check_victory.columnas):
                # Pongo min porque si el tablero no es de dimension n*n tiene que agarrar el lado mas chico así no tira Error de index
                x_shift = column
                y_shift = row
                minimun_iteration_over_diagonal = min(
                    self.tablero_to_check_victory.columnas - x_shift, self.tablero_to_check_victory.filas - y_shift)
                for diagonal_iterator in range(minimun_iteration_over_diagonal):
                    diagonal_iterator_x = diagonal_iterator + x_shift
                    diagonal_iterator_y = diagonal_iterator + y_shift
                    casillero_coordenadas = Coordenadas(
                        diagonal_iterator_x, diagonal_iterator_y)
                    self.decide_if_set_current_winner(casillero_coordenadas)
                if self._current_points >= self._points_to_win:
                    return self._current_winner

    def check_right_diagonal(self, list_of_teams: list[TeamTaTeTi]):
        for row in range(self.tablero_to_check_victory.filas):
            self._current_points = 0 
            self._current_winner = None
            for column in range(self.tablero_to_check_victory.columnas):
                # For right diagonals, we start from (column, row) and move up-right
                x_shift = column
                y_shift = row
                # Determine the maximum number of steps we can take in the diagonal direction
                minimun_iteration_over_diagonal = min(
                    x_shift + 1, self.tablero_to_check_victory.filas - y_shift)

                for diagonal_iterator in range(minimun_iteration_over_diagonal):
                    diagonal_iterator_x = x_shift - diagonal_iterator
                    diagonal_iterator_y = y_shift + diagonal_iterator
                    casillero_coordenadas = Coordenadas(
                        diagonal_iterator_x, diagonal_iterator_y)
                    self.decide_if_set_current_winner(casillero_coordenadas)
                    if self._current_points >= self._points_to_win:
                        return self._current_winner

    def check_empate(self, list_of_teams: list[TeamTaTeTi]):
        if self.tablero_to_check_victory.is_tablero_lleno():
            return list_of_teams

            
    def check_victory(self,list_of_teams: list[TeamTaTeTi] ):  # pasar el tablero aca, NO EN EL INIT
        column_win = self.check_column(list_of_teams)
        if column_win is not None:
            return column_win
        row_win = self.check_row(list_of_teams)
        if row_win is not None:
            return row_win
        left_diagonal_win = self.check_left_diagonal(list_of_teams)
        if left_diagonal_win is not None:
            return left_diagonal_win
        right_diagonal_win = self.check_right_diagonal(list_of_teams)
        if right_diagonal_win is not None:
            return right_diagonal_win
        empate = self.check_empate(list_of_teams)
        if empate:
            return empate
        return None
