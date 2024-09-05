from game.team import TeamTaTeTi
from game.fichas import FichaCruz

# TeamTurnHandler
# PlayerTurnHandler


class TurnHandler():
    def __init__(self, teams: list[TeamTaTeTi]):
        self._teams = teams
        self._current_team_turn = self.get_team_with_cross_piece()
        self._turn_index = 0
        self._sorted_list_of_teams = self.sort_list_of_teams_based_on_turns()

    def get_team_with_cross_piece(self):
        """Devuelve al equipo que juegue con la ficha de la Cruz"""
        for team in self._teams:
            if team.pieza_del_equipo == FichaCruz():
                return team

        # Si hay 2 fichas que no son la X devuelve el primer equipo
        return self._teams[0]

    def sort_list_of_teams_based_on_turns(self):
        sorted_list_of_teams = []
        team_with_cross_piece = self.get_team_with_cross_piece()
        # El primer turno siempre lo tiene el equipo con la pieza X
        sorted_list_of_teams.append(team_with_cross_piece)
        for team in self._teams:
            if team == team_with_cross_piece:
                continue
            sorted_list_of_teams.append(team)
        return sorted_list_of_teams

    def next_turn(self):
        if self._turn_index < len(self._teams)-1:
            self._turn_index += 1
        elif self._turn_index >= len(self._teams)-1:
            self._turn_index = 0
        self._current_team_turn = self._sorted_list_of_teams[self._turn_index]

    @property
    def turn_index(self):
        return self._turn_index

    @property
    def current_team_turn(self):
        return self._current_team_turn
