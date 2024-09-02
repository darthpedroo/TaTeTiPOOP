from abc import ABC
from tablero import Tablero, Coordenadas
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
                casillero_coordenadas = Coordenadas(col, row)
                casillero = self.tablero_to_check_victory.get_specific_casillero_from_coordenadas(
                    casillero_coordenadas)
                pieza = casillero.pieza
                print("pieza: ", casillero.pieza)
                print("col: ", casillero.columna)
                print("rwo: ", casillero.fila)
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
                casillero_coordenadas = Coordenadas(col, row)
                casillero = self.tablero_to_check_victory.get_specific_casillero_from_coordenadas(
                    casillero_coordenadas)
                pieza = casillero.pieza
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

    def check_left_diagonal(self):
        for row in range(self.tablero_to_check_victory.filas):
            for column in range(self.tablero_to_check_victory.columnas):
                current_winner = None
                current_points = 0
                # Pongo min porque si el tablero no es de dimension n*n tiene que agarrar el lado mas chico así no tira Error de index
                x_shift = column
                y_shift = row

                minimun_iteration_over_diagonal = min(
                    self.tablero_to_check_victory.columnas - x_shift, self.tablero_to_check_victory.filas - y_shift)

                for diagonal_iterator in range(minimun_iteration_over_diagonal):
                    diagonal_iterator_x = diagonal_iterator + x_shift
                    diagonal_iterator_y = diagonal_iterator + y_shift

                    pieza_coordenadas = Coordenadas(
                        diagonal_iterator_x, diagonal_iterator_y)

                    casillero = self.tablero_to_check_victory.get_specific_casillero_from_coordenadas(
                        pieza_coordenadas)
                    pieza = casillero.pieza
                  #  print("pieza:", pieza)
                   # print(
                    #   "col:", self.tablero_to_check_victory.tablero_matriz[diagonal_iterator_x][diagonal_iterator_y].columna)
                    # print(
                    #   "row: ", self.tablero_to_check_victory.tablero_matriz[diagonal_iterator_x][diagonal_iterator_y].fila)
                    if pieza is None:
                        current_winner = None
                        current_points = 0
                    elif pieza == current_winner:
                        current_points += 1
                    else:
                        current_winner = pieza
                        current_points = 1
                    if current_points >= self._points_to_win:
                        return current_winner

    def check_right_diagonal(self):
        for row in range(self.tablero_to_check_victory.filas):
            for column in range(self.tablero_to_check_victory.columnas):
                current_winner = None
                current_points = 0

                # For right diagonals, we start from (column, row) and move up-right
                x_shift = column
                y_shift = row

                # Determine the maximum number of steps we can take in the diagonal direction
                minimun_iteration_over_diagonal = min(
                    x_shift + 1, self.tablero_to_check_victory.filas - y_shift)

                for diagonal_iterator in range(minimun_iteration_over_diagonal):
                    diagonal_iterator_x = x_shift - diagonal_iterator
                    diagonal_iterator_y = y_shift + diagonal_iterator

                    pieza_coordenadas = Coordenadas(
                        diagonal_iterator_x, diagonal_iterator_y)
                    casillero = self.tablero_to_check_victory.get_specific_casillero_from_coordenadas(
                        pieza_coordenadas)
                    pieza = casillero.pieza

                    if pieza is None:
                        current_winner = None
                        current_points = 0
                    elif pieza == current_winner:
                        current_points += 1
                    else:
                        current_winner = pieza
                        current_points = 1

                    if current_points >= self._points_to_win:
                        return current_winner

        return None

    def check_victory(self):  # pasar el tablero aca, NO EN EL INIT

        print("pts:", self._points_to_win)
        column_win = self.check_column()
        if column_win is not None:
            return column_win
        row_win = self.check_row()
        if row_win is not None:
            return row_win
        left_diagonal_win = self.check_left_diagonal()
        if left_diagonal_win is not None:
            return left_diagonal_win

        right_diagonal_win = self.check_right_diagonal()
        if right_diagonal_win is not None:
            return right_diagonal_win

        return None
