from abc import ABC
from game.tablero import Tablero
from game.victoryhandler2 import TaTeTiVictoryHandler
from game.team import TeamTaTeTi
from game.fichas import FichaCirculo, FichaCruz, FichaSigma, FichaVater
from game.coordenadas import Coordenadas
from game.exceptions import CoordenadasFueraDelTablero, CasilleroOcupado, CoordenadasSonStr, CoordenadasNoSonPositivas
from game.player import Player
from game.turn_handler import TurnHandler


class TaTeTi():
    def __init__(self, tablero: Tablero, procesador_tablero, victory_handler: TaTeTiVictoryHandler, language: str = "ES") -> None:
        self._tablero = tablero
        self._procesador_tablero = procesador_tablero
        self._procesador_tablero.tablero_matriz = tablero  # CODE APESTOSITO
        self._tateti_victory_handler = victory_handler
        self._list_of_teams = []

        self._list_of_possible_pieces = [
            FichaCirculo(), FichaSigma(), FichaCruz(), FichaVater()]

        self._list_of_used_pieces = []

        # Language
        self._language = language
        self._turn_handler = None

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
                input("Cuántos equipos van a jugar?"))
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

    def seleccionar_ficha(self):
        ficha_class = None

        while ficha_class is None:
            print("FICHAS DISPONIBLES\n")
            for ficha in self._list_of_possible_pieces:
                if ficha not in self._list_of_used_pieces:
                    print(ficha.nombre, ficha.symbol,
                          "USAR ESTE IDENTIFICADOR PARA SELECCIONARLA: ", ficha.identificador, "\n")

            ficha_jugador_str = input(
                "Ingrese la ficha que quiere: \n").upper()

            # Search for the selected piece based on the identifier provided by the user
            for ficha2 in self._list_of_possible_pieces:
                if ficha2 not in self._list_of_used_pieces:
                    if ficha2.identificador == ficha_jugador_str:
                        self._list_of_used_pieces.append(ficha2)
                        ficha_class = ficha2
                        break  # Exit the loop once a valid ficha is found

            if ficha_class is None:
                print("ELIJA CORRECTAMENTE EL IDENTIFICADOR: \n")

        return ficha_class

    def create_team(self):
        nombre_equipo = input("Ingrese el nombre del equipo")
        cantidad_players_equipo = self.seleccionar_numero_jugadores_por_equipo()
        player_name_list = self.add_players_to_list(cantidad_players_equipo)
        ficha_class = self.seleccionar_ficha()
        team_temp = TeamTaTeTi(nombre_equipo, ficha_class, player_name_list)
        self._list_of_teams.append(team_temp)

    def menu_creacion_equipos(self):

        print("Bienvenido al TaTeTi")

        num_equipos = self.seleccionar_numero_equipos()

        for i in range(num_equipos):
            print(f"Creando el equipo num : {i+1}\n")
            self.create_team()

        self._turn_handler = TurnHandler(self.list_of_teams)

        print("Empieza el Juego")

    def empezar_partida(self):
        self._tablero.volver_a_crear_tablero()
        self._procesador_tablero.dibujar_tablero()
        self._list_of_used_pieces = []
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
        victory = None

        while victory is None:

            print("Turno de :", self._turn_handler.current_team_turn)

            valid_x_input = False
            valid_y_input = False

            while not valid_x_input and not valid_y_input:
                x_input = (input("Ingrese la columna\n"))
                y_input = (input("Ingrese la fila\n"))
                valid_x_input = self.is_input_a_valid_int(x_input)
                valid_y_input = self.is_input_a_valid_int(y_input)

            x_input = int(x_input)
            y_input = int(y_input)

            current_pieza = self._turn_handler.current_team_turn.pieza_del_equipo
            try:
                coordenadas = Coordenadas(x_input, y_input)
            except CoordenadasSonStr:
                print("HA INGRESADO UN STRING ! VUELVA A INGRESAR")
                self.poner_pieza()
            except CoordenadasNoSonPositivas:
                print("ERROR, INGRESE COORDENADAS POSITIVAS. ")
                self.poner_pieza()
            try:
                self._tablero.agregar_pieza_a_casillero_from_coordenadas(
                    coordenadas, current_pieza)
                casillero = self._tablero.get_specific_casillero_from_coordenadas(
                    coordenadas)

                victory = self._tateti_victory_handler.check_victory(
                    self._list_of_teams, self._tablero, casillero)

                print("VICTORY_ ", victory)

            except CasilleroOcupado:
                print("EL CASILLERO YA ESTA OCUPADO REY")
                self.poner_pieza()  # cambiar este codigo del diablo
            except CoordenadasFueraDelTablero:
                print("TUS CORDENADAS ESTAN FUERA DEL TABLERO, VOLVE A INGRESARLAS")
                self.poner_pieza()  # cambiar este codigo del diablo

            self._turn_handler.next_turn()
            self._procesador_tablero.dibujar_tablero()
        self.volver_a_jugar()

    def jugar(self):
        self.menu_creacion_equipos()
        self._procesador_tablero.dibujar_tablero()
        self.poner_pieza()
