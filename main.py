from juego import Juego, TableroConsola, TableroPygame

tablero_consola = TableroConsola()
tablero_pygame = TableroPygame()
juego = Juego(tablero_consola)
# juego.tablero = tablero_consola

seleccion = input("ELIJA SI QUIERE JUGAR EN LA CONSOLA 1) O EN PYGAME 2)")

if seleccion == "1":
    juego.tablero = tablero_consola
else:
    juego.tablero = tablero_pygame

juego.tablero.dibujar_tablero.dibujar_tablero()
