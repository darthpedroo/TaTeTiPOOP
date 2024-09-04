from juego import TaTeTi
from procesador import ProcesadorTableroConsola
from tablero import Tablero

tablero_ta_te_ti = Tablero(3, 3)
tablero_chess = Tablero(8, 8)
procesador_tablero_consola = ProcesadorTableroConsola()

ta_te_ti = TaTeTi(tablero_ta_te_ti, procesador_tablero_consola)
ta_te_ti.jugar()
