from abc import ABC
from game.tablero import Tablero
from game.victoryhandler import TaTeTiVictoryHandler
from game.team import TeamTaTeTi
from game.fichas import FichaCirculo, FichaCruz, FichaSigma, FichaVater, Placeable
from game.coordenadas import Coordenadas
from game.exceptions import CoordenadasFueraDelTablero, CasilleroOcupado, CoordenadasSonStr, CoordenadasNoSonPositivas
from game.player import Player
from game.turn_handler import TurnHandler
from game.helpers import is_input_a_valid_int, is_input_greater_than_zero


class TaTeTi():
    """Clase que maneja la lógica y los Inputs del Juego TaTeTi
    """

    def __init__(self, tablero: Tablero, procesador_tablero, victory_handler: TaTeTiVictoryHandler) -> None:
        self._tablero = tablero
        self._procesador_tablero = procesador_tablero
        self._procesador_tablero.tablero_matriz = tablero  # CODE APESTOSITO
        self._tateti_victory_handler = victory_handler
        self._list_of_teams = []
        self._list_of_possible_pieces = [
            FichaCirculo(), FichaSigma(), FichaCruz(), FichaVater()]
        self._list_of_used_pieces = []
        self._turn_handler = None

    @property
    def list_of_teams(self):
        return self._list_of_teams

    def seleccionar_numero_equipos(self) -> int:
        """Metodo para seleccionar el numero de equipos

        Returns:
            int: Numero de equipos
        """
        valid_input = False
        while not valid_input:
            num_equipos = (
                input("Cuántos equipos van a jugar?\n"))
            valid_input = is_input_greater_than_zero(num_equipos)
        num_equipos = int(num_equipos)
        return num_equipos

    def seleccionar_numero_jugadores_por_equipo(self) -> int:
        """Metododo para seleccionar el número de jugadores por equipo

        Returns:
            int: Numero de jugadores
        """

        valid_input = False
        while not valid_input:
            num_jugadores = input(
                "INGRESAR CANTIDAD DE JUGADORES DEL EQUIPO\n")
            valid_input = is_input_greater_than_zero(num_jugadores)
        num_jugadores = int(num_jugadores)
        return num_jugadores

    def add_players_to_list(self, cantidad_player_equipo: int) -> list[Player]:
        """Metodo para agregar una cantidad especifica de jugadores a la lista de equipos

        Args:
            cantidad_player_equipo (int): Cantidad de jugadores para meter al equipo

        Returns:
            list[Player]: Lista con los jugadores del equipo
        """
        player_name_list = []
        for i in range(cantidad_player_equipo):
            name = input(f"Ingrese el nombre del jugador {i+1} \n")
            player_name_list.append(name)
        return player_name_list

    def seleccionar_ficha(self) -> Placeable:
        """Metodo para seleccionar una ficha

        Returns:
            Placeable: La ficha seleccionada
        """

        ficha_class = None

        while ficha_class is None:
            print("FICHAS DISPONIBLES\n")
            for ficha in self._list_of_possible_pieces:
                if ficha not in self._list_of_used_pieces:
                    print(ficha.nombre, ficha.symbol,
                          "USAR ESTE IDENTIFICADOR PARA SELECCIONARLA: ", ficha.identificador, "\n")

            ficha_jugador_str = input(
                "Ingrese la ficha que quiere: \n").upper()

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
        """Método para crear un equipo"""

        valid_name = False
        while not valid_name:
            nombre_equipo = input("Ingrese el nombre del equipo\n")
            equipo_existe = False
            for team in self._list_of_teams:
                if team.nombre == nombre_equipo:
                    equipo_existe = True
                    break

            if equipo_existe:
                print("INGRESE UN NOMBRE DISTINTO AL DE SUS ADVERSARIOS")
            else:
                valid_name = True
                break

        cantidad_players_equipo = self.seleccionar_numero_jugadores_por_equipo()
        player_name_list = self.add_players_to_list(cantidad_players_equipo)
        ficha_class = self.seleccionar_ficha()
        team_temp = TeamTaTeTi(nombre_equipo, ficha_class, player_name_list)
        self._list_of_teams.append(team_temp)

    def menu_creacion_equipos(self):
        """Menu que muestra la creación de los equipos
        """

        print("Bienvenido al TaTeTi\n")

        num_equipos = self.seleccionar_numero_equipos()

        for i in range(num_equipos):
            print(f"Creando el equipo num : {i+1}\n")
            self.create_team()

        self._turn_handler = TurnHandler(self.list_of_teams)

        print("Empieza el Juego\n")

    def empezar_partida(self):
        """Metodo para empezar la partida
        """
        self._tablero.volver_a_crear_tablero()
        self._procesador_tablero.dibujar_tablero()
        self._list_of_used_pieces = []
        self.poner_pieza()

    def volver_a_jugar(self):
        """Metodo para volver a jugar
        """
        volver_a_jugar_input = input(
            "VOLVER A JUGAR?:\n 1) SI\n 2) NO\n").upper()

        print(volver_a_jugar_input)

        if volver_a_jugar_input == "SI":
            self.empezar_partida()
        elif volver_a_jugar_input == "NO":
            print("Gracias por jugar !")
        else:
            print("ESCRIBA CORRECTAMENTE SU INPUT\n")
            self.volver_a_jugar()

    def poner_pieza(self):
        """Logica para poner una pieza en el tablero
        """
        victory = None

        while victory is None:

            valid_x_input = False
            valid_y_input = False

            while not valid_x_input and not valid_y_input:
                x_input = (input("Ingrese la columna\n"))
                y_input = (input("Ingrese la fila\n"))
                valid_x_input = is_input_a_valid_int(x_input)
                valid_y_input = is_input_a_valid_int(y_input)

            x_input = int(x_input)
            y_input = int(y_input)

            current_pieza = self._turn_handler.current_team_turn.pieza_del_equipo
            try:
                coordenadas = Coordenadas(x_input, y_input)
            except CoordenadasSonStr:
                print("HA INGRESADO UN STRING ! VUELVA A INGRESAR\n")
                self.poner_pieza()
            except CoordenadasNoSonPositivas:
                print("ERROR, INGRESE COORDENADAS POSITIVAS. \n")
                self.poner_pieza()
            try:
                self._tablero.agregar_pieza_a_casillero_from_coordenadas(
                    coordenadas, current_pieza)
                casillero = self._tablero.get_specific_casillero_from_coordenadas(
                    coordenadas)

                victory = self._tateti_victory_handler.check_victory(
                    self._list_of_teams, self._tablero, casillero)

                if victory is not None:
                    if isinstance(victory, list):
                        print("EMPATE !")
                    else:
                        print("GANADOR EQUIPO: ", victory)

            except CasilleroOcupado:
                print("EL CASILLERO YA ESTA OCUPADO REY\n")
                self.poner_pieza()  # cambiar este codigo del diablo
            except CoordenadasFueraDelTablero:
                print("TUS CORDENADAS ESTAN FUERA DEL TABLERO, VOLVE A INGRESARLAS\n")
                self.poner_pieza()  # cambiar este codigo del diablo

            self._turn_handler.next_turn()
            self._procesador_tablero.dibujar_tablero()
        self.volver_a_jugar()

    def jugar(self):
        """Metodo para ejecutar el juego TaTeTi"""
        self.menu_creacion_equipos()
        self._procesador_tablero.dibujar_tablero()
        self.poner_pieza()
