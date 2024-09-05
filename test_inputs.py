import unittest
from unittest.mock import patch
from tablero import Tablero
from procesador import ProcesadorTableroConsola
from victoryhandler import TaTeTiVictoryHandler
from juego import TaTeTi


def get_user_name():
    name = input("Enter your name: ")
    return f"Hello, {name}!"


class TestUserInputTaTeTi(unittest.TestCase):

    def setUp(self):
        self.tablero_ta_te_ti = Tablero(3, 3)
        self.procesador_tablero_consola = ProcesadorTableroConsola()

        self.victory_handler = TaTeTiVictoryHandler(
            3, self.tablero_ta_te_ti)
        self.ta_te_ti = TaTeTi(self.tablero_ta_te_ti,
                               self.procesador_tablero_consola, self.victory_handler)

    @patch('builtins.input', side_effect=[
        'ES',          # LENGUAJE
        '2',           # NUMERO DE EQUIPOS QUE VAN A JUGAR
        # COMIENZA LA ELECCION DEL EQUIPO 1
        'Mega Rizz Team 1',  # NOMBRE TEAM 1
        '2',           # #CANTIDAD JUGADORES TEAM 1
        'Porky Player 1',    # NOMBRE PLAYER 1
        'Juanitrox Player 2',   # NOMBRE PLAYER2
        'X',           # FICHA ELEGIDA POR EL TEAM 1
        # COMIENZA LA ELECCION DEL EQUIPO 2
        'Sigma Sigma on The Wall Team 2',      # NOMBRE TEAM 2
        '2',           # CANTIDAD JUGADORES TEAM 2
        'Batman',    # NOMBRE PLAYER 1
        'Iron main',    # NOMBRE PLAYER 2
        'O',           # FICHA ELEGIDA POR EL TEAM 2
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
    ])
    def test01_partida_completa_jugada_con_test_de_inputs(self, mock_input):

        self.ta_te_ti.jugar()
        self.assertEqual(self.ta_te_ti.list_of_teams[0], self.victory_handler.check_victory(
            self.ta_te_ti.list_of_teams))


if __name__ == "__main__":
    unittest.main()
