from abc import ABC, abstractmethod
from fichas import Placeable, FichaCirculo


class Team(ABC):
    def __init__(self, nombre) -> None:
        self._nombre = nombre

    @property  # El metodo no es abstracto porque todas las sublcases de team van a acceder al property nombre de la misma manera
    def nombre(self):
        return self._nombre


class TeamTaTeTi(Team):
    def __init__(self, nombre: str, pieza_del_equipo: Placeable) -> None:
        super().__init__(nombre)
        self._pieza_del_equipo = pieza_del_equipo

    @property
    def pieza_del_equipo(self):
        return self._pieza_del_equipo


