import unittest
from unittest.mock import patch
from game.tablero import Tablero
from game.procesador import ProcesadorTableroConsola
from game.victoryhandler2 import TaTeTiVictoryHandler
from game.juego import TaTeTi
from game.fichas import FichaCruz, FichaSigma
from game.coordenadas import Coordenadas


def get_user_name():
    name = input("Enter your name: ")
    return f"Hello, {name}!"


class TestUserInputTaTeTi(unittest.TestCase):

    def setUp(self):
        self.tablero_ta_te_ti = Tablero(3, 3)
        self.procesador_tablero_consola = ProcesadorTableroConsola()

        self.victory_handler = TaTeTiVictoryHandler(
            3)
        self.ta_te_ti = TaTeTi(self.tablero_ta_te_ti,
                               self.procesador_tablero_consola, self.victory_handler)

    @patch('builtins.input', side_effect=[
        '2',           # NUMERO DE EQUIPOS QUE VAN A JUGAR
        # COMIENZA LA ELECCION DEL EQUIPO 1
        'Mega Rizz Team 1',  # NOMBRE TEAM 1
        '2',           # #CANTIDAD JUGADORES TEAM 1
        'Porky Player 1',    # NOMBRE PLAYER 1
        'Juanitrox Player 2',   # NOMBRE PLAYER2
        'V',           # FICHA ELEGIDA POR EL TEAM 1
        # COMIENZA LA ELECCION DEL EQUIPO 2
        'Sigma Sigma on The Wall Team 2',      # NOMBRE TEAM 2
        '2',           # CANTIDAD JUGADORES TEAM 2
        'Batman',    # NOMBRE PLAYER 1
        'Iron main',    # NOMBRE PLAYER 2
        'S',           # FICHA ELEGIDA POR EL TEAM 2
        # COMIENZAN LOS INPUTS DE SELECCION DE PIEZAS
        '0',
        '0',
        '0',
        '1',
        '1',
        '0',
        '1',
        '1',
        '2',
        '0',
        'dop',  # ME TIRA ERROR EL INPUT
        'si',
        # JUEGO LA MISMA PARTIDA DEVUELTA
        '0',
        '0',
        '0',
        '1',
        '1',
        '0',
        '1',
        '1',
        '2',
        '0',
        'no'
    ])
    def test01_partida_completa_jugada_con_test_de_inputs(self, mock_input):
        print("test01_partida_completa_jugada_con_test_de_inputs")
        self.ta_te_ti.jugar()
        last_casillero = self.tablero_ta_te_ti.get_specific_casillero_from_coordenadas(
            Coordenadas(2, 0))
        self.assertEqual(self.ta_te_ti.list_of_teams[1], self.victory_handler.check_victory(
            self.ta_te_ti.list_of_teams, self.tablero_ta_te_ti, last_casillero))

    @patch('builtins.input', return_value='S')
    def test_02_seleccionar_ficha(self, mock_input):
        ficha = self.ta_te_ti.seleccionar_ficha()
        self.assertEqual(ficha, FichaSigma())

    @patch('builtins.input', side_effect=[
        '2',           # NUMERO DE EQUIPOS QUE VAN A JUGAR
        # COMIENZA LA ELECCION DEL EQUIPO 1
        'Mega Rizz Team 1',  # NOMBRE TEAM 1
        '2',           # #CANTIDAD JUGADORES TEAM 1
        'Porky Player 1',    # NOMBRE PLAYER 1
        'Juanitrox Player 2',   # NOMBRE PLAYER2
        'V',           # FICHA ELEGIDA POR EL TEAM 1
        # COMIENZA LA ELECCION DEL EQUIPO 2
        'Sigma Sigma on The Wall Team 2',      # NOMBRE TEAM 2
        '2',           # CANTIDAD JUGADORES TEAM 2
        'Batman',    # NOMBRE PLAYER 1
        'Iron main',    # NOMBRE PLAYER 2
        'S',           # FICHA ELEGIDA POR EL TEAM 2
        # COMIENZAN LOS INPUTS DE SELECCION DE PIEZAS
        '0',
        '0',
        '0',
        '1',
        '1',
        '0',
        '1',
        '1',
        '2',
        '0',
        'dop',  # ME TIRA ERROR EL INPUT
        'si',
        # JUEGO LA MISMA PARTIDA DEVUELTA
        '0',
        '0',
        '0',
        '1',
        '1',
        '0',
        '1',
        '1',
        '2',
        '0',
        'no'
    ])
    def test03_partida_completa_jugada_con_test_de_inputs(self, mock_input):
        print("test01_partida_completa_jugada_con_test_de_inputs")
        self.ta_te_ti.jugar()
        self.assertRaises(ValueError)


if __name__ == "__main__":
    unittest.main()
