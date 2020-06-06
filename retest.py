import itertools
import sys
import numpy as np


def game_map():
    size = int(input('Enter the game size: '))
    if size < 3 or size > 7:
        print('Please chose between 3 and 7')
        game_map()
    else:
        map = np.zeros((size, size), dtype=int)
        return map


def win(game, won):
    # horizontal check
    for i in range(len(game[0])):
        if (np.max(game[i])) == (np.min(game[i])):
            if (np.max(game[i]) == 0) and (np.min(game[i]) == 0):
                pass
            else:
                print('All the row elements are same')
                won = True

    # vertical check
    for i in range(len(game[0])):
        if (np.max(game.T[i])) == (np.min(game.T[i])):
            if (np.max(game.T[i]) == 0) and (np.min(game.T[i]) == 0):
                pass
            else:
                print('All the column elements are same')
                won = True

    # diagonal check
    diag = np.zeros((1, 3), dtype=int)
    for i in range(len(game[0])):
        diag[0, i] = game[i][i]
        if np.max(diag) == np.min(diag):
            if (np.max(diag) == 0) and (np.min(diag) == 0):
                pass
            else:
                print('All the diagonal elements are same')
                won = True

    diag_opp = np.zeros((1, 3), dtype=int)
    for i in range(len(game[0])):
        diag_opp[0, i] = game[i][-i-1]
        if np.max(diag_opp) == np.min(diag_opp):
            if (np.max(diag) == 0) and (np.min(diag) == 0):
                pass
            else:
                print('All the diagonal elements are same')
                won = True
    return won


def board(game, row_choice, column_choice, current_player, game_size):
    if row_choice > (game_size - 1) or column_choice > (game_size - 1):
        print('Number exceeds play limit, please enter a valid choice')
        played = False
        return played
    if game[row_choice][column_choice] != 0:
        print('This position has already been taken, please choose a different one')
        played = False
    else:
        game[row_choice][column_choice] = current_player
        played = True
    return played


def another_game():
    yes = {'yes', 'y', 'ye', ''}
    no = {'no', 'n'}
    print('Press yes/no to restart the game:')
    choice = input().lower()
    if choice in yes:
        main()
    elif choice in no:
        return 0
    else:
        sys.stdout.write("Please respond with 'yes' or 'no'")
        another_game()


def main():
    won = False
    players = [1, 2]

    player_cycle = itertools.cycle(players)
    print(player_cycle)
    game = game_map()
    game_size = len(game[0])
    print(game)
    while not won:
        current_player = next(player_cycle)
        played = False

        while not played:
            print(f'current player : {current_player} ')
            row_choice = int(input('Which row: '))
            column_choice = int(input('Which column: '))
            played = board(game, row_choice, column_choice, current_player, game_size)
            print(f'')
            print(game)

        if win(game, won):
            print(f'{current_player} won the game')
            return 0
        else:
            if np.count_nonzero(game) == game.size:
                print('Match has been drawn')
                if not won:
                    another_game()
                    return 0
            won = False



if __name__ == '__main__':
    main()