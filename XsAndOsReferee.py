def checkio(game_result):
     
    # check row
    for row in game_result:
        if (row == 'XXX') or (row == 'OOO'):
            return row[0]
     
    # check col
    for i in range(0, 3):
        if (game_result[0][i] != '.') and (game_result[0][i] == game_result[1][i]) and (game_result[1][i] == game_result[2][i]):
            return game_result[0][i];
     
    # check diagonal
    if (game_result[1][1] != '.') and (game_result[0][0] == game_result[1][1]) and (game_result[1][1] == game_result[2][2]):
        return game_result[1][1]
    if (game_result[1][1] != '.') and (game_result[0][2] == game_result[1][1]) and (game_result[1][1] == game_result[2][0]):
        return game_result[1][1]
     
    # else
    return 'D'