from abc import ABC
from game.fichas import Placeable
from game.player import Player


class Team(ABC):
    """Clase abstacta para todos los Teams que puedan existir en un juego
    """

    def __init__(self, nombre) -> None:
        self._nombre = nombre

    @property  # El metodo no es abstracto porque todas las sublcases de team van a acceder al property nombre de la misma manera
    def nombre(self):
        return self._nombre

    def __eq__(self, other):
        """
        Checkea que dos instancias de Team tengan el mismo nombre
        Args:
            other (Team): La otra instancia de Team con la que comparar el nombre.

        Returns:
            bool: Devuelve True si el nombre es el mismo, devuelve False si son distintos
        """
        if self._nombre == other._nombre:
            return True
        return False

    def __str__(self):
        return self._nombre


class TeamTaTeTi(Team):
    """
    Clase que representa un equipo del TaTeTi

    Attributes:
        nombre (str): nombre del equipo.
        pieza_del_equipo (Placeable): pieza con la que juega el equipo.
        identificador (list[Player]): players en el equipo.
    """

    def __init__(self, nombre: str, pieza_del_equipo: Placeable, players: list[Player]) -> None:
        super().__init__(nombre)
        self._pieza_del_equipo = pieza_del_equipo
        self._players = players

    @property
    def pieza_del_equipo(self):
        return self._pieza_del_equipo

    @property
    def players(self):
        return self._players
