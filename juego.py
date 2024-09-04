from abc import ABC
import sys
from tablero import Tablero
from victoryhandler import TaTeTiVictoryHandler
from team import TeamTaTeTi
from fichas import FichaCirculo, FichaCruz
from json_translator import JSONTranslator
from coordenadas import Coordenadas


class TaTeTi():
    def __init__(self, tablero: Tablero, procesador_tablero, victory_handler: TaTeTiVictoryHandler, language:str = "ES") -> None:
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
    
    def empezar_juego(self):
        for i in self._json_translator.list_of_languages:
            print(f"LANGUAGE: [{i}]")
        selected_language = input("ELIJA UN LENGUAGE DE LOS DE ARRIBA:")
        self._json_translator.set_language(selected_language)        
        print(self._json_translator.read_json("bienvenido"))
        num_equipos = None
        while not isinstance(num_equipos, int):
            try:
                num_equipos = int(input(self._json_translator.read_json("num_equipos")))
            except ValueError:
                num_equipos = int(input(self._json_translator.read_json("num_equipos")))
        
        for i in range(num_equipos):
            nombre_equipo = input(self._json_translator.read_json("nombre_equipo"))
            ficha_class = None    
            while ficha_class is None:
                ficha_jugador_str = input(self._json_translator.read_json("ficha_jugador_str")).capitalize()
                if ficha_jugador_str == "X":
                    ficha_class = FichaCruz()
                elif ficha_jugador_str == "O":
                    ficha_class = FichaCirculo()
                else:
                    print(self._json_translator.read_json("error_ficha_invalida"))
            team_temp = TeamTaTeTi(nombre_equipo, ficha_class)
            self._list_of_teams.append(team_temp)
        print(self._json_translator.read_json("empezar_juego"))


    def jugar(self):
        self.empezar_juego()
        victory = False
        pieza_team_1 = self.list_of_teams[0].pieza_del_equipo
        pieza_team_2 = self.list_of_teams[1].pieza_del_equipo #Hacer que esto acepte más de 2 equipo
        turno = 1
        

        while not victory:
            self._procesador_tablero.dibujar_tablero()
            turno+=1
            if turno%2 == 0:
                print(f"Turno del equipo: {self.list_of_teams[0].nombre}")
                curr_pieza = pieza_team_1
            else:
                print(f"Turno del equipo: {self.list_of_teams[1].nombre}")
                curr_pieza = pieza_team_2


            x_input = int(input("Ingrese la columna\n")) 
            y_input = int(input("Ingrese la fila\n"))
            coordenadas = Coordenadas(x_input, y_input)

            self._tablero.agregar_pieza_a_casillero_from_coordenadas(
            coordenadas, curr_pieza)
            victory = self._tateti_victory_handler.check_victory(self._list_of_teams)
        
        print("victoria de: ", victory)

