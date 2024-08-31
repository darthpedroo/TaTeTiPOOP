import unittest
from tablero import Tablero, Coordenadas
from juego import TaTeTi, ProcesadorTableroConsola
from fichas import FichaCirculo, FichaCruz


class TestTaTeTi(unittest.TestCase):

    def setUp(self):
        self.tablero_ta_te_ti = Tablero(3, 3)
        self.procesador_tablero_consola = ProcesadorTableroConsola()
        self.ta_te_ti = TaTeTi(self.tablero_ta_te_ti,
                               self.procesador_tablero_consola)


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
        new_casillero = self.tablero_ta_te_ti.get_specific_casillero_from_coordenadas(
            coordenadas)
        self.assertEqual(
            self.tablero_ta_te_ti._tablero_matriz[x][y], new_casillero)

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


if __name__ == "__main__":
    unittest.main()
