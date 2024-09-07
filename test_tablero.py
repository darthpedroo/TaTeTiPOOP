import unittest

from game.tablero import Tablero
from game.coordenadas import Coordenadas
from game.exceptions import CoordenadasFueraDelTablero, CasilleroOcupado, CoordenadasNoSonPositivas, CoordenadasSonStr
from game.procesador import ProcesadorTableroConsola
from game.fichas import FichaCirculo


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

    def test_07_tablero_lleno(self):
        print("test_07_tablero_lleno")
        curr_pieza = FichaCirculo()

        for columnas in range(self.tablero_ta_te_ti.columnas):
            for filas in range(self.tablero_ta_te_ti.filas):
                coordenadas = Coordenadas(columnas, filas)
                self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
                    coordenadas, curr_pieza)
                self.procesador_tablero_consola.dibujar_tablero()

        self.assertTrue(self.tablero_ta_te_ti.is_tablero_lleno())

    def test_08_tablero_incompleto(self):
        print("test_08_tablero_incompleto")
        curr_pieza = FichaCirculo()

        for columnas in range(self.tablero_ta_te_ti.columnas-1):
            for filas in range(self.tablero_ta_te_ti.filas-1):
                coordenadas = Coordenadas(columnas, filas)
                self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
                    coordenadas, curr_pieza)
                self.procesador_tablero_consola.dibujar_tablero()

        self.assertFalse(self.tablero_ta_te_ti.is_tablero_lleno())

    def test_09_coordenadas_no_son_int_tira_error(self):
        print("test_09_coordenadas_no_son_int_tira_error")
        curr_pieza = FichaCirculo()
        x = "-0"
        y = -230
        with self.assertRaises(CoordenadasSonStr):
            coordenadas = Coordenadas(x, y)
            self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
                coordenadas, curr_pieza)

    def test_10_coordenadas_no_son_positivas_tira_error(self):
        curr_pieza = FichaCirculo()
        x = -10
        y = -230
        with self.assertRaises(CoordenadasNoSonPositivas):
            coordenadas = Coordenadas(x, y)
            self.tablero_ta_te_ti.agregar_pieza_a_casillero_from_coordenadas(
                coordenadas, curr_pieza)


if __name__ == "__main__":
    unittest.main()
