import unittest
from game.tablero import Tablero
from game.coordenadas import Coordenadas
from game.exceptions import CoordenadasFueraDelTablero, CasilleroOcupado, CoordenadasNoSonPositivas, CoordenadasSonStr
from game.juego import TaTeTi
from game.procesador import ProcesadorTableroConsola
from game.fichas import FichaCirculo, FichaCruz
from game.victoryhandler import TaTeTiVictoryHandler
from game.team import TeamTaTeTi
from game.player import Player


class TestTaTeTiVictoryHandler3puntosVictory3x3(unittest.TestCase):
    def setUp(self):
        self.tablero_ta_te_ti = Tablero(3, 3)
        self.teams = [TeamTaTeTi("Papu Gigante", FichaCruz(), [Player("Porky")]), TeamTaTeTi(
            "Mega Rizzlers", FichaCirculo(), [Player("Beni")])]
        self.victory_handler = TaTeTiVictoryHandler(
            3)
        self.procesador_tablero_consola = ProcesadorTableroConsola(
            self.tablero_ta_te_ti)
        self.ta_te_ti = TaTeTi(self.tablero_ta_te_ti,
                               self.procesador_tablero_consola, self.victory_handler)
        self.ta_te_ti._list_of_teams = self.teams

    def test_09_diagonal_derecha_win_no_deberia_dar_error(self):
        current_pieza = self.teams[1].pieza_del_equipo

        x1 = 0
        x2 = 0
        x3 = 1

        y1 = 1
        y2 = 2
        y3 = 1

        mov1_coordenadas = Coordenadas(x1, y1)
        mov2_coordenadas = Coordenadas(x2, y2)
        mov3_coordenadas = Coordenadas(x3, y3)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov1_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov2_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov3_coordenadas, current_pieza)
        self.procesador_tablero_consola.dibujar_tablero()
        self.assertEqual(self.teams[1], self.victory_handler.check_victory(
            self.ta_te_ti.list_of_teams))


if __name__ == "__main__":
    unittest.main()
