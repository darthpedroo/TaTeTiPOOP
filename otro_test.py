import unittest
from tablero import Tablero, Coordenadas, CasilleroOcupado, CoordenadasFueraDelTablero
from juego import TaTeTi, ProcesadorTableroConsola
from fichas import FichaCirculo, FichaCruz
from victoryhandler import TaTeTiVictoryHandler
from team import TeamTaTeTi


class TestTaTeTi(unittest.TestCase):

    def setUp(self):
        self.tablero_ta_te_ti = Tablero(3, 3)
        self.procesador_tablero_consola = ProcesadorTableroConsola()
        self.teams = [TeamTaTeTi("Papu Gigante", FichaCruz()), TeamTaTeTi(
            "Mega Rizzlers", FichaCirculo())]
        self.victory_handler = TaTeTiVictoryHandler(
            3, self.tablero_ta_te_ti, self.teams)
        self.ta_te_ti = TaTeTi(self.tablero_ta_te_ti,
                               self.procesador_tablero_consola, self.victory_handler)

    def test_01_partida_1_vs_1(self):
        print("test_01_partida_1_vs_1")
        pieza_j1 = self.teams[0].pieza_del_equipo
        pieza_j2 = self.teams[1].pieza_del_equipo

        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p1 = Coordenadas(1, 2)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p1, pieza_j1)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()


        mov_p2 = Coordenadas(2, 2)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p2, pieza_j2)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()


        mov_p1 = Coordenadas(0, 0)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p1, pieza_j1)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()


        mov_p2 = Coordenadas(0, 1)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p2, pieza_j2)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()


        mov_p1 = Coordenadas(1, 1)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p1, pieza_j1)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p2 = Coordenadas(1, 0)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p2, pieza_j2)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p1 = Coordenadas(2, 0)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p1, pieza_j1)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p2 = Coordenadas(0, 2)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p2, pieza_j2)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        mov_p1 = Coordenadas(2, 1)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p1, pieza_j1)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()


        self.assertEqual(self.teams, self.victory_handler.check_victory())

if __name__ == "__main__":
    unittest.main()
