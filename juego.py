from abc import ABC
import sys
from tablero import Tablero
from victoryhandler import TaTeTiVictoryHandler
from team import TeamTaTeTi
from fichas import FichaCirculo, FichaCruz




class TaTeTi():
    def __init__(self, tablero: Tablero, procesador_tablero, victory_handler: TaTeTiVictoryHandler) -> None:
        self._tablero = tablero
        self._procesador_tablero = procesador_tablero
        self._procesador_tablero.tablero_matriz = tablero
        self._tateti_victory_handler = victory_handler
        self._tateti_victory_handler.tablero_to_check_victory = self._tablero
        self._tateti_victory_handler.list_of_teams = [
            TeamTaTeTi("Papu Gigante", FichaCruz()), TeamTaTeTi("Mega Rizzlers", FichaCirculo())]

    def jugar(self):
        self._procesador_tablero.dibujar_tablero()
