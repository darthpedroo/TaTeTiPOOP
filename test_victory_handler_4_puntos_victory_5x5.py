import unittest
from unittest.mock import patch

from game.tablero import Tablero
from game.coordenadas import Coordenadas
from game.exceptions import CoordenadasFueraDelTablero, CasilleroOcupado, CoordenadasNoSonPositivas, CoordenadasSonStr
from game.juego import TaTeTi
from game.procesador import ProcesadorTableroConsola
from game.fichas import FichaCirculo, FichaCruz, FichaSigma
from game.victoryhandler2 import TaTeTiVictoryHandler
from game.team import TeamTaTeTi
from game.player import Player


class TaTeTiVictoryHandler4puntosVictory5x5(unittest.TestCase):
    def setUp(self):
        puntos_para_ganar = 4
        self.tablero_ta_te_ti = Tablero(5, 5)
        self.teams = [TeamTaTeTi("Papu Gigante", FichaCruz(), [Player("Porky")]), TeamTaTeTi(
            "Mega Rizzlers", FichaCirculo(), [Player("Beni")])]
        self.victory_handler = TaTeTiVictoryHandler(
            puntos_para_ganar)
        self.procesador_tablero_consola = ProcesadorTableroConsola(
            self.tablero_ta_te_ti)
        self.ta_te_ti = TaTeTi(self.tablero_ta_te_ti,
                               self.procesador_tablero_consola, self.victory_handler)
        self.ta_te_ti._list_of_teams = self.teams

    def test_01_check_left_diagonal_win(self):
        print("test_01_check_left_diagonal_win")
        current_pieza = self.teams[1].pieza_del_equipo
        x1 = 2
        x2 = 3
        x3 = 4
        y1 = 1
        y2 = 2
        y3 = 3
        x4 = 1
        y4 = 0
        mov1_coordenadas = Coordenadas(x1, y1)
        mov2_coordenadas = Coordenadas(x2, y2)
        mov3_coordenadas = Coordenadas(x3, y3)
        mov4_coordenadas = Coordenadas(x4, y4)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov1_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov2_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov3_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov4_coordenadas, current_pieza)
        self.procesador_tablero_consola.dibujar_tablero()

        last_casillero = self.tablero_ta_te_ti.get_specific_casillero_from_coordenadas(
            mov4_coordenadas)

        self.assertEqual(self.teams[1], self.victory_handler.check_victory(
            self.ta_te_ti.list_of_teams, self.tablero_ta_te_ti, last_casillero))

    def test_02_check_right_diagonal_win(self):
        print("test_01_check_left_diagonal_win")
        current_pieza = self.teams[1].pieza_del_equipo
        x1 = 4
        x2 = 3
        x3 = 2
        x4 = 1

        y1 = 0
        y2 = 1
        y3 = 2
        y4 = 3

        mov1_coordenadas = Coordenadas(x1, y1)
        mov2_coordenadas = Coordenadas(x2, y2)
        mov3_coordenadas = Coordenadas(x3, y3)
        mov4_coordenadas = Coordenadas(x4, y4)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov1_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov2_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov3_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov4_coordenadas, current_pieza)
        self.procesador_tablero_consola.dibujar_tablero()
        last_casillero = self.tablero_ta_te_ti.get_specific_casillero_from_coordenadas(
            mov4_coordenadas)

        self.assertEqual(self.teams[1], self.victory_handler.check_victory(
            self.ta_te_ti.list_of_teams, self.tablero_ta_te_ti, last_casillero))

    def test_02_check_right_diagonal_win_desfasado(self):
        print("test_02_check_right_diagonal_win_offset_down")
        current_pieza = self.teams[1].pieza_del_equipo
        x1 = 4
        x2 = 3
        x3 = 2
        x4 = 1

        y1 = 1
        y2 = 2
        y3 = 3
        y4 = 4

        mov1_coordenadas = Coordenadas(x1, y1)
        mov2_coordenadas = Coordenadas(x2, y2)
        mov3_coordenadas = Coordenadas(x3, y3)
        mov4_coordenadas = Coordenadas(x4, y4)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov1_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov2_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov3_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov4_coordenadas, current_pieza)
        self.procesador_tablero_consola.dibujar_tablero()
        last_casillero = self.tablero_ta_te_ti.get_specific_casillero_from_coordenadas(
            mov4_coordenadas)

        self.assertEqual(self.teams[1], self.victory_handler.check_victory(
            self.ta_te_ti.list_of_teams, self.tablero_ta_te_ti, last_casillero))

    def test_03_check_right_diagonal_win_desfasado_2(self):
        print("test_03_check_right_diagonal_win_offset_right")
        current_pieza = self.teams[1].pieza_del_equipo
        x1 = 3
        x2 = 2
        x3 = 1
        x4 = 0

        y1 = 0
        y2 = 1
        y3 = 2
        y4 = 3

        mov1_coordenadas = Coordenadas(x1, y1)
        mov2_coordenadas = Coordenadas(x2, y2)
        mov3_coordenadas = Coordenadas(x3, y3)
        mov4_coordenadas = Coordenadas(x4, y4)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov1_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov2_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov3_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov4_coordenadas, current_pieza)
        self.procesador_tablero_consola.dibujar_tablero()
        last_casillero = self.tablero_ta_te_ti.get_specific_casillero_from_coordenadas(
            mov4_coordenadas)

        self.assertEqual(self.teams[1], self.victory_handler.check_victory(
            self.ta_te_ti.list_of_teams, self.tablero_ta_te_ti, last_casillero))


if __name__ == "__main__":
    unittest.main()
