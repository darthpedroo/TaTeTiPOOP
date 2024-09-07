from abc import ABC


class Placeable(ABC):
    """Contenedor abstacta para todo lo que se pueda poner sobre el tablero

        Esta clase sirve como base para definir varios tipos de placeables en el tablero
    """

    def __init__(self):
        pass


class TaTeTiFicha(Placeable):
    """
    Representa una ficha del TaTeTi.

    Attributes:
        nombre (str): nombre de la pieza.
        symbol (str): simbolo de la pieza.
        identificador (str): identificador que se usa para seleccionar la pieza.
    """

    def __init__(self, nombre: str, symbol: str, identificador: str):
        self._nombre = nombre
        self._symbol = symbol
        self._identificador = identificador

    def __eq__(self, other: 'TaTeTiFicha') -> bool:
        """
        Checkea que dos instancias de TaTeTiFicha tengan el mismo symbolo
        Args:
            other (TaTeTiFicha): La otra instancia de TaTeTiFicha con la que comparar el symbolo.

        Returns:
            bool: Devuelve True si el symnbolo es el mismo, devuelve False si son distinto
        """
        if other is None:
            return False
        if self._symbol == other._symbol:
            return True
        return False

    @property
    def nombre(self):
        return self._nombre

    @property
    def symbol(self):
        return self._symbol

    @property
    def identificador(self):
        return self._identificador


class FichaCirculo(TaTeTiFicha):
    def __init__(self):
        super().__init__(nombre="Circulo", symbol="[O]", identificador="O")


class FichaSigma(TaTeTiFicha):
    def __init__(self):
        super().__init__(nombre="SigmaFace", symbol="[🗿]", identificador="S")


class FichaCruz(TaTeTiFicha):
    def __init__(self):
        super().__init__(nombre="Cruz", symbol="[X]", identificador="X")


class FichaVater(TaTeTiFicha):
    def __init__(self):
        super().__init__(nombre="Vater", symbol="[🚽]", identificador="V")
