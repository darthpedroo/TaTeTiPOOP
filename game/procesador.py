from game.tablero import Tablero


class ProcesadorTableroConsola():
    """Clase que sirve para procesar la Clase Tablero en la consola"""

    def __init__(self, tablero: Tablero | None = None) -> None:
        # Puede ser None Esto? Porque no deberia serlo aunque le hago dsp el setter
        self._tablero_matriz = tablero

    @property
    def tablero_matriz(self):
        return self._tablero_matriz

    @tablero_matriz.setter
    def tablero_matriz(self, new_tablero):
        self._tablero_matriz = new_tablero

    def dibujar_tablero(self):
        """Dibuja la matriz del tablero en la consola"""
        print("\n")
        for row in self._tablero_matriz:
            print(row)
        print("\n")
