class CasilleroOcupado(Exception):
    def __init__(self):
        super().__init__("El Casillero Está Ocupado")

class CoordenadasFueraDelTablero(Exception):
    def __init__(self):
        super().__init__("Las coordenadas ingresadas se encuentran fuera del tablero")