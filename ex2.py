import itertools
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]


def win(thisGame):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
        
    for row in thisGame:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally")
            return True

    
    for col in range(len(thisGame[0])):
        check = []
        for row in thisGame:
            check.append(row[col])

        if all_same(check):
            print(f"Player {check[0]} is the winner vertically")
            return True

    check_diag = []
    for diag in range(len(thisGame[0])):
        check_diag.append(thisGame[diag][diag])

    if all_same(check_diag):
        print(f"Player {check_diag[0]} is the winner")
        return True

    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        diags.append(game[idx][reverse_idx])

    if all_same(diags):
        print(f"Player {diags[0]} has won Diagonally (/)")
        return True
        
        
        
def board(game_map, player, row, column):
    if game_map[row][column] != 0:
        print('This is already chosen, play another')
        return False
    
    game_map[row][column] = player
    print("   0  1  2")
    for count,row in enumerate(game_map):
        print(count,row)
    return game_map

won = False
players = [1, 2]
player_cycle = itertools.cycle(players)
while not won:
    current_player = next(player_cycle)
    played = False 
    while not played:
        print(f"Player: {current_player}")
        row_choice = int(input('which row: '))
        column_choice = int(input('which column: '))
        played = board(game, player=current_player, row=row_choice, column=column_choice)
        
        if win(game):
            print('Game Over')
            won = True            
