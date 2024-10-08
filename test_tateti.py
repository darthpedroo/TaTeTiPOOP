import unittest

from game.tablero import Tablero
from game.coordenadas import Coordenadas
from game.juego import TaTeTi
from game.procesador import ProcesadorTableroConsola
from game.fichas import FichaCirculo, FichaCruz
from game.victoryhandler import TaTeTiVictoryHandler
from game.team import TeamTaTeTi
from game.player import Player


class TestTaTeTi(unittest.TestCase):

    def setUp(self):
        self.tablero_ta_te_ti = Tablero(3, 3)
        self.procesador_tablero_consola = ProcesadorTableroConsola()
        self.teams = [TeamTaTeTi("Papu Gigante", FichaCruz(), [Player("Porky")]), TeamTaTeTi(
            "Mega Rizzlers", FichaCirculo(), [Player("Beni")])]

        self.victory_handler = TaTeTiVictoryHandler(
            3)

        self.ta_te_ti = TaTeTi(self.tablero_ta_te_ti,
                               self.procesador_tablero_consola, self.victory_handler)
        self.ta_te_ti._list_of_teams = self.teams

    def test_01_partida_1_vs_1_gana_equipo_0(self):
        print("test_01_partida_1_vs_1")
        pieza_j1 = self.teams[0].pieza_del_equipo
        pieza_j2 = self.teams[1].pieza_del_equipo

        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p1 = Coordenadas(1, 2)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p1, pieza_j1)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p2 = Coordenadas(0, 0)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p2, pieza_j2)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p1 = Coordenadas(2, 2)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p1, pieza_j1)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p2 = Coordenadas(0, 1)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p2, pieza_j2)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p1 = Coordenadas(0, 2)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p1, pieza_j1)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        last_casillero = self.tablero_ta_te_ti.get_specific_casillero_from_coordenadas(
            mov_p1)

        self.assertEqual(
            self.teams[0], self.ta_te_ti._tateti_victory_handler.check_victory(self.ta_te_ti.list_of_teams, self.tablero_ta_te_ti, last_casillero))

    def test_02_empate_partida_1_vs_1(self):
        print("test_02_empate_partida_1_vs_1")
        pieza_j1 = self.teams[0].pieza_del_equipo
        pieza_j2 = self.teams[1].pieza_del_equipo

        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p1 = Coordenadas(0, 0)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p1, pieza_j1)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p2 = Coordenadas(0, 1)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p2, pieza_j2)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p1 = Coordenadas(0, 2)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p1, pieza_j1)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p2 = Coordenadas(1, 0)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p2, pieza_j2)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p1 = Coordenadas(1, 1)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p1, pieza_j1)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p2 = Coordenadas(1, 2)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p2, pieza_j2)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p1 = Coordenadas(2, 0)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p1, pieza_j1)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p2 = Coordenadas(2, 1)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p2, pieza_j2)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p1 = Coordenadas(2, 2)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p1, pieza_j2)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        last_casillero = self.tablero_ta_te_ti.get_specific_casillero_from_coordenadas(
            mov_p1)

        self.assertEqual(
            self.teams, self.ta_te_ti._tateti_victory_handler.check_victory(self.ta_te_ti.list_of_teams, self.tablero_ta_te_ti, last_casillero))


if __name__ == "__main__":
    unittest.main()
