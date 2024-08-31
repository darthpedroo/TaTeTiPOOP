from abc import ABC
import pygame
import sys
from tablero import Tablero


class ProcesadorTableroConsola():
    def __init__(self) -> None:
        # Puede ser None Esto? Porque no deberia serlo aunque le hago dsp el setter
        self._tablero_matriz = None

    @property
    def tablero_matriz(self):
        return self._tablero_matriz

    @tablero_matriz.setter
    def tablero_matriz(self, new_tablero):
        self._tablero_matriz = new_tablero

    def dibujar_tablero(self):
        for row in self._tablero_matriz:
            print(row)


class TaTeTi():
    def __init__(self, tablero: Tablero, procesador_tablero) -> None:
        self._tablero = tablero
        self._procesador_tablero = procesador_tablero
        self._procesador_tablero.tablero_matriz = tablero

    def jugar(self):
        self._procesador_tablero.dibujar_tablero()
