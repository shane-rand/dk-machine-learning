from __future__ import division
from NFL_Lineup_Generator import NFLLineupGenerator
from NFLGeneralMultipliers import *
import numpy
import csv
from constants import *
from Logger import get_logger

logger = get_logger()

# taking ratio between projected_points / ppg then std_dev + min projected_points

TEAM_BLACKLIST = ()
PLAYER_BLACKLIST = ()


def NFLFormulaFour(lineup, player_holder):
    if not NFLLineupGenerator.lineup_under_salary_cap(lineup):
        return -100000
    else:
        fitness = get_lineup_player_scores(lineup)
        team_multiplier = get_team_multiplier(lineup)
        games_multiplier = get_game_multiplier(lineup, player_holder.games)
        black_list_multipler = get_blacklist_muiltiplier(lineup, PLAYER_BLACKLIST, TEAM_BLACKLIST)
        return fitness * team_multiplier * games_multiplier * black_list_multipler

def get_player_score(player):
    if not player.projected_points:
        return -100
    if player.projected_points < 5:
        return -100
    if player.ppg <= 5:
        return -100
    matchup_coefficient = float(get_matchup_coefficient(player))
    new_points = (player.projected_points * matchup_coefficient)
    return new_points

def get_matchup_coefficient(player):
    coef = 0
    if player.position == "WR" or player.position == "QB":
        coef = PASS_DEFENSE_COEFFICIENTS[player.opponent]
    elif player.position == "RB":
        coef = RUSH_DEFENSE_COEFFICIENTS[player.opponent]
    return (1 + (float(coef) / 2))

def get_lineup_player_scores(lineup):
    fitness = []
    for p in lineup:
        fitness_score = get_player_score(p)
        fitness.append(fitness_score)
        p.special_stat = fitness_score
    return sum(fitness) #* (numpy.std(numpy.array(fitness))/ sum(fitness))