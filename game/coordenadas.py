

    
class Coordenadas():
    """Clase que representa coordenadas en el tablero.

    Attributes:
        x (int): La posición en la columna del tablero (eje X).
        y (int): La posición en la fila del tablero (eje Y).
    """

    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y