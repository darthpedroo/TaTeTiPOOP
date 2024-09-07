import unittest

from game.tablero import Tablero
from game.coordenadas import Coordenadas
from game.juego import TaTeTi
from game.procesador import ProcesadorTableroConsola
from game.fichas import FichaCirculo, FichaCruz, FichaSigma
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

    def test_01_1_columna_3_del_tablero_completa_equipo_2(self):
        print("test_01_1_columna_3_del_tablero_completa_equipo_2")
        current_pieza = self.teams[1].pieza_del_equipo
        enemy_pieza = self.teams[0].pieza_del_equipo
        x = 2
        y1 = 0
        y2 = 1
        y3 = 2
        mov1_coordenadas = Coordenadas(x, y1)
        mov2_coordenadas = Coordenadas(x, y2)
        mov3_coordenadas = Coordenadas(x, y3)
        mov4_coordenadas = Coordenadas(0, 2)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov1_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov4_coordenadas, enemy_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov2_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov3_coordenadas, current_pieza)
        self.procesador_tablero_consola.dibujar_tablero()

        last_casillero = self.tablero_ta_te_ti.get_specific_casillero_from_coordenadas(
            mov3_coordenadas)

        self.assertEqual(
            self.teams[1], self.victory_handler.check_victory(self.ta_te_ti.list_of_teams, self.tablero_ta_te_ti, last_casillero))

    def test_02_fila_1_del_tablero_completa_equipo_2(self):
        current_pieza = self.teams[1].pieza_del_equipo
        x1 = 0
        x2 = 1
        x3 = 2
        y = 0
        mov1_coordenadas = Coordenadas(x1, y)
        mov2_coordenadas = Coordenadas(x2, y)
        mov3_coordenadas = Coordenadas(x3, y)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov1_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov2_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov3_coordenadas, current_pieza)

        self.procesador_tablero_consola.dibujar_tablero()

        last_casillero = self.tablero_ta_te_ti.get_specific_casillero_from_coordenadas(
            mov3_coordenadas)

        self.assertEqual(self.teams[1], self.victory_handler.check_victory(
            self.ta_te_ti.list_of_teams, self.tablero_ta_te_ti, last_casillero))

    def test_03_fila_2_del_tablero_completa_equipo_2(self):
        current_pieza = self.teams[1].pieza_del_equipo
        x1 = 0
        x2 = 1
        x3 = 2
        y = 1
        mov1_coordenadas = Coordenadas(x1, y)
        mov2_coordenadas = Coordenadas(x2, y)
        mov3_coordenadas = Coordenadas(x3, y)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov1_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov2_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov3_coordenadas, current_pieza)

        self.procesador_tablero_consola.dibujar_tablero()

        last_casillero = self.tablero_ta_te_ti.get_specific_casillero_from_coordenadas(
            mov3_coordenadas)

        self.assertEqual(self.teams[1], self.victory_handler.check_victory(
            self.ta_te_ti.list_of_teams, self.tablero_ta_te_ti, last_casillero))

    def test_04_fila_3_del_tablero_completa_equipo_2(self):
        current_pieza = self.teams[1].pieza_del_equipo
        x1 = 0
        x2 = 1
        x3 = 2
        y = 2
        mov1_coordenadas = Coordenadas(x1, y)
        mov2_coordenadas = Coordenadas(x2, y)
        mov3_coordenadas = Coordenadas(x3, y)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov1_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov2_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov3_coordenadas, current_pieza)
        self.procesador_tablero_consola.dibujar_tablero()
        last_casillero = self.tablero_ta_te_ti.get_specific_casillero_from_coordenadas(
            mov3_coordenadas)

        self.assertEqual(self.teams[1], self.victory_handler.check_victory(
            self.ta_te_ti.list_of_teams, self.tablero_ta_te_ti, last_casillero))

    def test_05_columna_1_del_tablero_completa_equipo_2(self):
        print("test_05_columna_1_del_tablero_completa_equipo_2")
        current_pieza = self.teams[1].pieza_del_equipo
        x = 0
        y1 = 0
        y2 = 1
        y3 = 2
        mov1_coordenadas = Coordenadas(x, y1)
        mov2_coordenadas = Coordenadas(x, y2)
        mov3_coordenadas = Coordenadas(x, y3)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov1_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov2_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov3_coordenadas, current_pieza)
        self.procesador_tablero_consola.dibujar_tablero()
        last_casillero = self.tablero_ta_te_ti.get_specific_casillero_from_coordenadas(
            mov3_coordenadas)

        self.assertEqual(self.teams[1], self.victory_handler.check_victory(
            self.ta_te_ti.list_of_teams, self.tablero_ta_te_ti, last_casillero))

    def test_06_columna_2_del_tablero_completa_equipo_2(self):
        print("test_06_columna_2_del_tablero_completa_equipo_2")
        current_pieza = self.teams[1].pieza_del_equipo
        x = 1
        y1 = 0
        y2 = 1
        y3 = 2
        mov1_coordenadas = Coordenadas(x, y1)
        mov2_coordenadas = Coordenadas(x, y2)
        mov3_coordenadas = Coordenadas(x, y3)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov1_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov2_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov3_coordenadas, current_pieza)
        self.procesador_tablero_consola.dibujar_tablero()
        last_casillero = self.tablero_ta_te_ti.get_specific_casillero_from_coordenadas(
            mov3_coordenadas)

        self.assertEqual(self.teams[1], self.victory_handler.check_victory(
            self.ta_te_ti.list_of_teams, self.tablero_ta_te_ti, last_casillero))

    def test_07_columna_3_del_tablero_completa_equipo_2(self):
        print("test_07_columna_3_del_tablero_completa_equipo_2")
        current_pieza = self.teams[1].pieza_del_equipo
        x = 2
        y1 = 0
        y2 = 1
        y3 = 2
        mov1_coordenadas = Coordenadas(x, y1)
        mov2_coordenadas = Coordenadas(x, y2)
        mov3_coordenadas = Coordenadas(x, y3)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov1_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov2_coordenadas, current_pieza)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            mov3_coordenadas, current_pieza)
        self.procesador_tablero_consola.dibujar_tablero()
        last_casillero = self.tablero_ta_te_ti.get_specific_casillero_from_coordenadas(
            mov3_coordenadas)

        self.assertEqual(self.teams[1], self.victory_handler.check_victory(
            self.ta_te_ti.list_of_teams, self.tablero_ta_te_ti, last_casillero))

    def test_08_diagonal_izquierda_victoria(self):
        print("test_08_diagonal")
        current_pieza = self.teams[1].pieza_del_equipo
        x1 = 0
        x2 = 1
        x3 = 2
        y1 = 0
        y2 = 1
        y3 = 2
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
        last_casillero = self.tablero_ta_te_ti.get_specific_casillero_from_coordenadas(
            mov3_coordenadas)

        self.assertEqual(self.teams[1], self.victory_handler.check_victory(
            self.ta_te_ti.list_of_teams, self.tablero_ta_te_ti, last_casillero))


if __name__ == "__main__":
    unittest.main()
