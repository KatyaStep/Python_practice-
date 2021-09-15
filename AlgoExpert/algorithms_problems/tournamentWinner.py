from collections import defaultdict

def tournamentWinner(competitions, results):
    winners = defaultdict(int)
    homeTeam_winner = 1
    homeTeam_idx = 0
    awayTeam_idx = 1
    score = 3

    for i in range(len(results)):
        if results[i] == homeTeam_winner:
            winners[competitions[i][homeTeam_idx]] += score
        else:
            winners[competitions[i][awayTeam_idx]] += score

    for team, score in winners.items():
        if score == max(winners.values()):
            return team



competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
]
results = [0, 0, 1]

print(tournamentWinner(competitions, results))