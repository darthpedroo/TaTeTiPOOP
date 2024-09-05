from game.juego import TaTeTi
from game.procesador import ProcesadorTableroConsola
from game.tablero import Tablero
from game.victoryhandler import TaTeTiVictoryHandler

tablero_ta_te_ti = Tablero(3, 3)
tablero_chess = Tablero(8, 8)
procesador_tablero_consola = ProcesadorTableroConsola()
victory_handler = TaTeTiVictoryHandler(3, tablero_ta_te_ti)

ta_te_ti = TaTeTi(tablero_ta_te_ti,
                  procesador_tablero_consola, victory_handler)
ta_te_ti.jugar()
