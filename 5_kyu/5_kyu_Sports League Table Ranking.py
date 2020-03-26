""" All tasks come from www.codewars.com """

"""
TASK: Sports League Table Ranking

Description
You organize a sports league in a round-robin-system. Each team meets all other teams. 
In your league a win gives a team 2 points, a draw gives both teams 1 point. 
After some games you have to compute the order of the teams in your league. 

You use the following criteria to arrange the teams:
1) Points
2) Scoring differential (the difference between goals scored and those conceded)
3) Goals scored

First you sort the teams by their points. 
If two or more teams reached the same number of points, the second criteria comes into play and so on. 
Finally, if all criteria are the same, the teams share a place.

Input
number: Number of teams in your league.
games: An array of arrays. Each item represents a played game with an array of four elements 
[TeamA,TeamB,GoalA,GoalB] (TeamA played against TeamB and scored GoalA goals and conceded GoalB goals ).

Output
positions: An array of positions. The i-th item should be the position of the i-th team in your league.

number = 6
games = [[0, 5, 2, 2],   // Team 0 - Team 5 => 2:2
         [1, 4, 0, 2],   // Team 1 - Team 4 => 0:2
         [2, 3, 1, 2],   // Team 2 - Team 3 => 1:2
         [1, 5, 2, 2],   // Team 1 - Team 5 => 2:2
         [2, 0, 1, 1],   // Team 2 - Team 0 => 1:1
         [3, 4, 1, 1],   // Team 3 - Team 4 => 1:1
         [2, 5, 0, 2],   // Team 2 - Team 5 => 0:2
         [3, 1, 1, 1],   // Team 3 - Team 1 => 1:1
         [4, 0, 2, 0]]   // Team 4 - Team 0 => 2:0

You may compute the following table:

Rank	Team	For : Against	GD	Points
1.	    Team 4	  5 : 1	        +4	5
2.	    Team 5	  6 : 4	        +2	4
3.	    Team 3	  4 : 3	        +1	4
4.	    Team 0	  3 : 5	        -2	2
4.	    Team 1	  3 : 5	        -2	2
6.	    Team 2	  2 : 5	        -3	1
Team 5 and Team 3 reached the same number of points. But since Team 5 got a better scoring differential, it ranks better than Team 3. 
All values of Team 0 and Team 1 are the same, so these teams share the fourth place.

In this example you have to return the array [4, 4, 6, 3, 1, 2].
"""

import pandas as pd

WIN = 2
DRAW = 1


def compute_ranks(number, games):
    # Table with games
    df = pd.DataFrame(games)
    df.columns = ['TeamA', 'TeamB', 'GoalA', 'GoalB']

    # Create list of teams
    teams = [['Team' + str(i)] for i in range(number)]

    # Create new table for calculate points
    score_df = pd.DataFrame(teams)
    score_df['Points'] = 0
    score_df['For'] = 0
    score_df['Against'] = 0

    # Calculate points
    for index, row in df.iterrows():
        if row[2] > row[3]:
            scored_team = row[0]
            score_df.loc[scored_team, 'Points'] += WIN
            score_df.loc[scored_team, 'For'] += row[2]
            score_df.loc[scored_team, 'Against'] += row[3]
        elif row[2] < row[3]:
            scored_team = row[1]
            score_df.loc[scored_team, 'Points'] += WIN
            score_df.loc[scored_team, 'For'] += row[3]
            score_df.loc[scored_team, 'Against'] += row[2]
        elif row[2] == row[3]:
            first_team = row[0]
            second_team = row[1]
            score_df.loc[first_team, 'Points'] += DRAW
            score_df.loc[second_team, 'Points'] += DRAW
            score_df.loc[first_team, 'For'] += row[2]
            score_df.loc[first_team, 'Against'] += row[3]
            score_df.loc[second_team, 'For'] += row[3]
            score_df.loc[second_team, 'Against'] += row[2]

    # Calculate GD based on gols score
    score_df['GD'] = score_df['For'] - score_df['Against']

    # Calculate Rank
    score_df["Rank"] = score_df[["Points", "GD"]].apply(tuple, axis=1) \
        .rank(method='min', ascending=False).astype(int)

    return list(score_df['Rank'])


# Another option

import numpy as np
from scipy.stats import rankdata as rd

WIN = 2
DRAW = 1


def compute_ranks(number, games):
    teams = np.zeros((number, 3))

    # Table with teams
    for team_a, team_b, points_a, points_b in games:
        teams[team_a, 1] += points_a
        teams[team_a, 2] += points_a - points_b
        teams[team_b, 1] += points_b
        teams[team_b, 2] += points_b - points_a

        if points_a == points_b:
            teams[team_a, 0] += DRAW
            teams[team_b, 0] += DRAW
        elif points_a > points_b:
            teams[team_a, 0] += WIN
        else:
            teams[team_b, 0] += WIN

    team_scores = teams.dot(np.array([-100000, -1, -1000]).reshape(-1, 1))
    return rd(team_scores, method='min').astype(int).tolist()


# Top solution

from collections import namedtuple

TeamScore = namedtuple('TeamScore', 'pts team')


def compute_ranks(nTeams, games):
    def updateCnts(t, g1, g2):
        cnts[t].pts[0] += 1 + (g1 > g2) - (g1 < g2)
        cnts[t].pts[1] += g1 - g2
        cnts[t].pts[2] += g1

    cnts = [TeamScore([0, 0, 0], t) for t in range(nTeams)]
    for tA, tB, gA, gB in games:
        updateCnts(tA, gA, gB)
        updateCnts(tB, gB, gA)
    cnts.sort(reverse=True)

    out = [0] * nTeams
    for i, (pts, t) in enumerate(cnts):
        if not i or pts != cnts[i - 1].pts: rnk = i + 1
        out[t] = rnk

    return out

