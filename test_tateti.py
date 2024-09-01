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

        self.assertEqual(
            None, self.ta_te_ti._tateti_victory_handler.check_victory())

        mov_p2 = Coordenadas(0, 0)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p2, pieza_j2)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        self.assertEqual(
            None, self.ta_te_ti._tateti_victory_handler.check_victory())

        mov_p1 = Coordenadas(2, 2)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p1, pieza_j1)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        self.assertEqual(
            None, self.ta_te_ti._tateti_victory_handler.check_victory())

        mov_p2 = Coordenadas(0, 1)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p2, pieza_j2)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()
        self.assertEqual(
            None, self.ta_te_ti._tateti_victory_handler.check_victory())

        mov_p1 = Coordenadas(0, 2)
        self.ta_te_ti._tablero.agregar_pieza_a_casillero_from_coordenadas(
            mov_p1, pieza_j1)
        self.ta_te_ti._procesador_tablero.dibujar_tablero()

        self.assertEqual(
            pieza_j1, self.ta_te_ti._tateti_victory_handler.check_victory())


class TestTablero(unittest.TestCase):

    def setUp(self):
        self.tablero_ta_te_ti = Tablero(3, 3)
        self.tablero_ta_te_ti.crear_tablero()
        self.procesador_tablero_consola = ProcesadorTableroConsola(
            self.tablero_ta_te_ti)

    def test_01_get_casillero_from_coordenadas(self):
        print("test_01_get_casillero_from_coordenadas")
        x = 0
        y = 0
        coordenadas = Coordenadas(x, y)
        new_casillero = self.tablero_ta_te_ti.get_specific_casillero_from_coordenadas(
            coordenadas)
        self.assertEqual(
            self.tablero_ta_te_ti._tablero_matriz[x][y], new_casillero)

    def test_02_get_casillero_from_coordenadas_tira_error(self):
        print("test_02_get_casillero_from_coordenadas_tira_error")
        x = 0
        y = 12
        coordenadas = Coordenadas(x, y)
        with self.assertRaises(CoordenadasFueraDelTablero):
            new_casillero = self.tablero_ta_te_ti.get_specific_casillero_from_coordenadas(
                coordenadas)

    def test_03_agregar_pieza_a_casillero_from_coordenadas(self):
        print("test_03_agregar_pieza_a_casillero_from_coordenadas")
        curr_pieza = FichaCirculo()
        x = 0
        y = 0
        coordenadas = Coordenadas(x, y)
        self.procesador_tablero_consola.dibujar_tablero()
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            coordenadas, curr_pieza)
        self.procesador_tablero_consola.dibujar_tablero()

    def test_04_borrar_pieza_a_casillero_from_coordenadas(self):
        print("test_04_borrar_pieza_a_casillero_from_coordenadas")
        curr_pieza = FichaCirculo()
        x = 0
        y = 0
        coordenadas = Coordenadas(x, y)
        self.procesador_tablero_consola.dibujar_tablero()
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            coordenadas, curr_pieza)
        self.procesador_tablero_consola.dibujar_tablero()
        self.tablero_ta_te_ti.borrar_pieza_a_casillero_from_coordenadas(
            coordenadas)
        self.procesador_tablero_consola.dibujar_tablero()

    def test_05_agregar_pieza_a_casillero_ocupado_tira_error(self):
        print("test_05_agregar_pieza_a_casillero_ocupado_tira_error")
        curr_pieza = FichaCirculo()
        x = 0
        y = 0
        coordenadas = Coordenadas(x, y)
        self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
            coordenadas, curr_pieza)
        with self.assertRaises(CasilleroOcupado):
            self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
                coordenadas, curr_pieza)

    def test_06_agregar_pieza_con_coordenadas_fuera_del_tablero_tira_error(self):
        print("test_06_agregar_pieza_con_coordenadas_fuera_del_tablero_tira_error")
        curr_pieza = FichaCirculo()
        x = 0
        y = 12323
        coordenadas = Coordenadas(x, y)

        with self.assertRaises(CoordenadasFueraDelTablero):
            self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
                coordenadas, curr_pieza)

    def test_06_borrar_pieza_con_coordenadas_fuera_del_tablero_tira_error(self):
        print("test_06_borrar_pieza_con_coordenadas_fuera_del_tablero_tira_error")
        x = 0
        y = 230
        coordenadas = Coordenadas(x, y)
        with self.assertRaises(CoordenadasFueraDelTablero):
            self.tablero_ta_te_ti.borrar_pieza_a_casillero_from_coordenadas(
                coordenadas)


class TestJugador(unittest.TestCase):
    def test_01_caca(self):
        pass


class TestTaTeTiVictoryHandler(unittest.TestCase):
    def setUp(self):
        self.tablero_ta_te_ti = Tablero(5, 5)
        self.teams = [TeamTaTeTi("Papu Gigante", FichaCruz()), TeamTaTeTi(
            "Mega Rizzlers", FichaCirculo())]
        self.victory_handler = TaTeTiVictoryHandler(
            3, self.tablero_ta_te_ti, self.teams)
        self.procesador_tablero_consola = ProcesadorTableroConsola(
            self.tablero_ta_te_ti)

    def test_01_get_list_of_pieces_from_team(self):
        print("test_01_get_list_of_pieces_from_team")
        print("PIEZAS ACTUALES: ",
              self.victory_handler.get_list_of_pieces_from_team())

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
        print("Ganador:", self.victory_handler.check_victory())
        self.assertEqual(
            current_pieza, self.victory_handler.check_victory())

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

        print("Ganador:", self.victory_handler.check_victory())
        self.assertEqual(current_pieza, self.victory_handler.check_victory())

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

        print("Ganador:", self.victory_handler.check_victory())
        self.assertEqual(current_pieza, self.victory_handler.check_victory())

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
        print("Ganador:", self.victory_handler.check_victory())
        self.assertEqual(current_pieza, self.victory_handler.check_victory())

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
        print("Ganador:", self.victory_handler.check_victory())
        self.assertEqual(
            current_pieza, self.victory_handler.check_victory())

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
        print("Ganador:", self.victory_handler.check_victory())
        self.assertEqual(
            current_pieza, self.victory_handler.check_victory())

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
        print("Ganador:", self.victory_handler.check_victory())
        self.assertEqual(
            current_pieza, self.victory_handler.check_victory())


if __name__ == "__main__":
    unittest.main()
