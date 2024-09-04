import unittest
from tablero import Tablero
from coordenadas import Coordenadas
from exceptions import CoordenadasFueraDelTablero, CasilleroOcupado
from juego import TaTeTi
from procesador import ProcesadorTableroConsola
from fichas import FichaCirculo, FichaCruz
from victoryhandler import TaTeTiVictoryHandler
from team import TeamTaTeTi


class TestTaTeTi(unittest.TestCase):

    def test_01_dop(self):
        pass


if __name__ == "__main__":
    unittest.main()
