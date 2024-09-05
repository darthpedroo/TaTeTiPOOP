from abc import ABC
from game.tablero import Tablero
from game.victoryhandler import TaTeTiVictoryHandler
from game.team import TeamTaTeTi
from game.fichas import FichaCirculo, FichaCruz
from game.json_translator import JSONTranslator
from game.coordenadas import Coordenadas
from game.exceptions import CoordenadasFueraDelTablero, CasilleroOcupado
from game.player import Player
from game.turn_handler import TurnHandler


class TaTeTi():
    def __init__(self, tablero: Tablero, procesador_tablero, victory_handler: TaTeTiVictoryHandler, language: str = "ES") -> None:
        self._tablero = tablero
        self._procesador_tablero = procesador_tablero
        self._procesador_tablero.tablero_matriz = tablero
        self._tateti_victory_handler = victory_handler
        self._tateti_victory_handler.tablero_to_check_victory = self._tablero
        self._list_of_teams = []
        self._language = language
        self._json_translator = JSONTranslator()

    @property
    def list_of_teams(self):
        return self._list_of_teams

    def is_input_a_valid_int(self, input):
        try:
            int(input)
        except ValueError:
            print("INGRESA UN NÚMERO, NO UN TEXTO")
            return False
        if int(input) < 0:
            print("INGRESA UN NÚMERO POSITIVO")
            return False
        return True

    def seleccionar_numero_equipos(self):
        valid_input = False
        while not valid_input:
            num_equipos = (
                input(self._json_translator.read_json("num_equipos")))
            valid_input = self.is_input_a_valid_int(num_equipos)
        num_equipos = int(num_equipos)
        return num_equipos

    def seleccionar_numero_jugadores_por_equipo(self):
        valid_input = False
        while not valid_input:
            num_jugadores = input(
                "INGRESAR CANTIDAD DE JUGADORES DEL EQUIPO\n")
            valid_input = self.is_input_a_valid_int(num_jugadores)
        num_jugadores = int(num_jugadores)
        return num_jugadores

    def add_players_to_list(self, cantidad_player_equipo: int) -> list[Player]:
        player_name_list = []
        for i in range(cantidad_player_equipo):
            name = input(f"Ingrese el nombre del jugador {i+1} \n")
            player_name_list.append(name)
        return player_name_list

    def create_team(self):
        nombre_equipo = input(self._json_translator.read_json("nombre_equipo"))
        cantidad_players_equipo = self.seleccionar_numero_jugadores_por_equipo()
        player_name_list = self.add_players_to_list(cantidad_players_equipo)
        ficha_class = None
        while ficha_class is None:
            ficha_jugador_str = input(self._json_translator.read_json(
                "ficha_jugador_str")).capitalize()
            print("ficha_jugador", ficha_jugador_str)
            if ficha_jugador_str == "X":
                ficha_class = FichaCruz()
            elif ficha_jugador_str == "O":
                ficha_class = FichaCirculo()
            else:
                print(self._json_translator.read_json("error_ficha_invalida"))
        team_temp = TeamTaTeTi(nombre_equipo, ficha_class, player_name_list)
        self._list_of_teams.append(team_temp)

    def menu_creacion_equipos(self):
        for i in self._json_translator.list_of_languages:
            print(f"LANGUAGE: [{i}]")
        selected_language = input("ELIJA UN LENGUAGE DE LOS DE ARRIBA:")
        self._json_translator.set_language(selected_language)
        print(self._json_translator.read_json("bienvenido"))

        num_equipos = self.seleccionar_numero_equipos()

        for i in range(num_equipos):
            print(f"Creando el equipo num : {i+1}\n")
            self.create_team()
        print(self._json_translator.read_json("empezar_juego"))

    def empezar_partida(self):
        self._tablero.volver_a_crear_tablero()
        self._procesador_tablero.dibujar_tablero()
        self.poner_pieza()

    def volver_a_jugar(self):
        volver_a_jugar_input = input(
            "VOLVER A JUGAR?:\n 1) SI\n 2) NO\n").upper()

        print(volver_a_jugar_input)

        if volver_a_jugar_input == "SI":
            self.empezar_partida()
        elif volver_a_jugar_input == "NO":
            print("Gracias por jugar !")
        else:
            print("ESCRIBA CORRECTAMENTE SU INPUT")
            self.volver_a_jugar()

    def poner_pieza(self):
        victory = False
        turn_handler = TurnHandler(self.list_of_teams)

        while not victory:
            print("Turno de :", turn_handler.current_team_turn)
            x_input = int(input("Ingrese la columna\n"))
            y_input = int(input("Ingrese la fila\n"))
            current_pieza = turn_handler.current_team_turn.pieza_del_equipo
            try:
                coordenadas = Coordenadas(x_input, y_input)
            except CoordenadasFueraDelTablero:
                print("TUS CORDENADAS ESTAN FUERA DEL TABLERO, VOLVE A INGRESARLAS")
                self.poner_pieza()  # cambiar este codigo del diablo
            try:
                self._tablero.agregar_pieza_a_casillero_from_coordenadas(
                    coordenadas, current_pieza)
                victory = self._tateti_victory_handler.check_victory(
                    self._list_of_teams)
            except CasilleroOcupado:
                print("EL CASILLERO YA ESTA OCUPADO REY")
                self.poner_pieza()  # cambiar este codigo del diablo
            turn_handler.next_turn()
            self._procesador_tablero.dibujar_tablero()

        self.volver_a_jugar()

    def jugar(self):
        self.menu_creacion_equipos()
        self._procesador_tablero.dibujar_tablero()
        self.poner_pieza()
