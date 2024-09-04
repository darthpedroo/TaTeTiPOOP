from abc import ABC, abstractmethod
from fichas import Placeable, FichaCirculo
from player import Player


class Team(ABC):
    def __init__(self, nombre) -> None:
        self._nombre = nombre

    @property  # El metodo no es abstracto porque todas las sublcases de team van a acceder al property nombre de la misma manera
    def nombre(self):
        return self._nombre
    
    def __eq__(self, other):
        if self._nombre == other._nombre: #IMPLEMENTAR QUE NO SE PUEDA REPETIR UN NOMBRE EN UN EQUIPO :v
            return True
        return False
    
    def __str__(self):
        return self._nombre

class TeamTaTeTi(Team):
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

