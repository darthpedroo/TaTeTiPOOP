from abc import ABC
import pygame
import sys


class DibujarTableroConsola():
    def __init__(self, tablero_matriz: list[list]) -> None:
        self._tablero_matriz = tablero_matriz

    def dibujar_tablero(self):
        for row in self._tablero_matriz:
            print(row)


class DibujarTableroPygame:
    def __init__(self, tablero_matriz: list[list], cell_size: int = 50) -> None:
        self._tablero_matriz = tablero_matriz
        self._cell_size = cell_size
        self._width = len(tablero_matriz[0]) * cell_size
        self._height = len(tablero_matriz) * cell_size

    def dibujar_tablero(self):
        pygame.init()
        screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption("Tablero Pygame")
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Clear screen with white background
            screen.fill((255, 255, 255))

            for y, row in enumerate(self._tablero_matriz):
                for x, cell in enumerate(row):
                    pygame.draw.rect(
                        screen,
                        (0, 0, 0),  # Color of the cell border
                        pygame.Rect(x * self._cell_size, y * self._cell_size,
                                    self._cell_size, self._cell_size),
                        1  # Border width
                    )
                    font = pygame.font.Font(None, 36)
                    text_surf = font.render(
                        str(cell), True, (0, 0, 0))  # Text color
                    text_rect = text_surf.get_rect(center=(x * self._cell_size + self._cell_size // 2,
                                                           y * self._cell_size + self._cell_size // 2))
                    screen.blit(text_surf, text_rect)

            pygame.display.flip()
            clock.tick(60)


class Tablero(ABC):
    pass


class TableroConsola(Tablero):
    def __init__(self) -> None:
        self._tablero_matriz = [["-", "-", "-"],
                                ["-", "-", "-"], ["-", "-", "-"]]
        self._dibujar_tablero = DibujarTableroConsola(self._tablero_matriz)

    @property
    def dibujar_tablero(self):
        return self._dibujar_tablero


class TableroPygame(Tablero):
    def __init__(self) -> None:
        self._tablero_matriz = [["-", "-", "-"],
                                ["-", "-", "-"], ["-", "-", "-"]]
        self._dibujar_tablero = DibujarTableroPygame(self._tablero_matriz)

    @property
    def dibujar_tablero(self):
        return self._dibujar_tablero


class Juego():
    def __init__(self, tablero: Tablero) -> None:
        self._tablero = tablero

    @property
    def tablero(self):
        return self._tablero

    @tablero.setter
    def tablero(self, tablero: Tablero):
        self._tablero = tablero
