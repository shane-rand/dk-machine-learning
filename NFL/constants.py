import csv
from Logger import get_logger

logger = get_logger()

BASE_PATH = "data/"

PASS_DEFENSE_COEFFICIENTS = {}
RUSH_DEFENSE_COEFFICIENTS = {}


def createMatchupCoefficients():
    file_path = BASE_PATH + "dvoa-10_14.csv"
    with open(file_path, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == "rank":
                continue
            PASS_DEFENSE_COEFFICIENTS[row[1]] = row[8]
            RUSH_DEFENSE_COEFFICIENTS[row[1]] = row[11]
createMatchupCoefficients()

TEAM_MATCHER = {
    'Green Bay': 'Packers',
    'Los Angeles': 'Rams',
    'Kansas City': 'Chiefs',
    'New York': 'Jets',
    'New England': 'Patriots',
    'New York': 'Giants',
    'Tampa Bay': 'Buccaneers',
    'San Francisco': '49ers',
    'New Orleans': 'Saints',
    'San Diego': 'Chargers'
}

SALARY_CAP = 50000

POSITIONS = ['QB', 'RB', 'WR', 'TE', 'DST']

NFL_FAN_POSITIONS = ['QB', 'RB', 'WR', 'TE', 'DEF']

POSITIONS_WITH_FLEX = ['QB', 'RB', 'WR', 'TE', 'DST', 'FLEX']

FLEX_POSITIONS = ['RB', 'WR', 'TE']

VALID_LINEUP_POSITIONS = {
    'QB': 1,
    'RB': 2,
    'WR': 3,
    'TE': 1,
    'FLEX': 1,
    'DST': 1
}

FFPRO = 'http://www.fantasypros.com/nfl/projections/'

def GET_ITERABLE_VALID_LINEUP():
    return [key for key, val in VALID_LINEUP_POSITIONS.items() for _ in range(0, val)]
