'''
    Sample Input: 
        competitions: [
                ['Bulls', 'Lakers']
                ['Lakers', 'Celtics'],
                ['Celtics', 'Bulls']
            ]
        results = [0, 0, 1] 
    
    *** competitions[0] = ['Home Team', 'Away Team']
    *** results: 0 - Away Win, 1 - Home Win
'''

def tournament_winner(competitions, results):
    current_leader = ''
    scores = {}

    for idx, competition in enumerate(competitions):
        home_team, away_team = competition

        winner = home_team if results[idx] == 1 else away_team

        scores[winner] = scores.get(winner, 0) + 3

        if scores[winner] > scores.get(current_leader, 0):
            current_leader = winner

    return current_leader


competitions= [ ['Bulls', 'Lakers'], ['Lakers', 'Celtics'], ['Celtics', 'Bulls'] ]
results = [0, 0, 1] 

print( tournament_winner(competitions, results) )