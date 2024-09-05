from game.exceptions import CoordenadasSonStr, CoordenadasNoSonPositivas


class Coordenadas():
    """Clase que representa coordenadas en el tablero.

    Attributes:
        x (int): La posición en la columna del tablero (eje X).
        y (int): La posición en la fila del tablero (eje Y).
    """

    def __init__(self, x, y) -> None:
        self.validate_coordinates(x, y)
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def validate_coordinates(self, x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            raise CoordenadasSonStr()
        if x < 0 or y < 0:
            raise CoordenadasNoSonPositivas()
