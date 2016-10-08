def sort_players(players, key = "elo_std"):
    players.sort([(key, -1)])
    return players
