

class NFLPlayer():

    def __init__(self, name, team, position, salary, ppg, opp, projected_points=None):
        self.name = name
        self.team = team
        self.position = position
        self.salary = salary
        self.ppg = ppg
        self.opponent = opp
        self.projected_points = projected_points

    def update_projected_points(self, points):
        self.projected_points = points

    def update_opponent(self, opp):
        self.opponent = opp