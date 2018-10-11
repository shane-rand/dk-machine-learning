import csv
from NFL_Player import NFLPlayer
from Logger import get_logger

logger = get_logger()

BASE_PATH = "data/"

def get_all_players(file_path):
    file_path = BASE_PATH + file_path
    players = []
    with open(file_path, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == "Position":
                continue
            team = row[5]
            game_string = row[3]
            if team == _get_team_one(game_string):
                opp = _get_team_two(game_string)
            else:
                opp = _get_team_one(game_string)
            players.append(NFLPlayer(row[1], row[5], row[0], int(row[2]), float(row[4]), opp))
    return players

def get_all_games(file_path):
    file_path = BASE_PATH + file_path
    games = []
    with open(file_path, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == "Position":
                continue
            game = _game_parser(row[3])
            if game not in games:
                games.append(game)
    return games

def get_all_projections(file_path):
    file_path = BASE_PATH + file_path
    projections = []
    with open(file_path, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == 'playername':
                continue
            name = ""
            name_split = row[0].split(" ")
            for x in range(0, len(name_split)):
                if x >= len(name_split) - 2:
                    if not name_split[x].isupper():
                        name += name_split[x] + " "
                else:
                    name += name_split[x] + " "
            name = name.rstrip()
            projections.append([name, row[1]])
    return projections


def _game_parser(game_string):
    first_team = game_string.split("@")[0]
    second_team = game_string.split("@")[1].split(" ")[0]
    return (first_team, second_team)

def _get_team_one(game_string):
    first_team = game_string.split("@")[0]
    return first_team

def _get_team_two(game_string):
    second_team = game_string.split("@")[1].split(" ")[0]
    return second_team