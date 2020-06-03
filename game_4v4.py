import itertools
import numpy as np
import sys


# Take only column as input if the number below is still zero then
# the number takes that place

def fill_map(board, column, player):
    for i in reversed(range(len(board[0]))):
        if board[i][column] == 0:
            board[i][column] = player
            played = True
            return played
        elif board[0][column] != 0:
            print(f'{column} is full')
            played = False
            return played
        else:
            continue


def win(board, players, won):
    # horizontal
    for i in reversed(range(len(board[0]))):
        counter1 = 0
        counter2 = 0
        for j in reversed(range(len(board[0]))):
            if board[i][j] == players[0]:
                counter1 = counter1 + 1
                if counter1 == 4:
                    print(f'{players[0]} is the winner')
                    won = True
                    return won
            else:
                counter1 = 0
                won = False

            if board[i][j] == players[1]:
                counter2 = counter2 + 1
                if counter2 == 4:
                    print(f'{players[1]} is the winner')
                    won = True
                    return won
            else:
                counter2 = 0
                won = False


    # Vertiacal
    for i in reversed(range(len(board[0]))):
        counter1 = 0
        counter2 = 0
        for j in reversed(range(len(board[0]))):
            if board[j][i] == players[0]:
                counter1 = counter1 + 1
                if counter1 == 4:
                    print(f'{players[0]} is the winner')
                    won = True
                    return won
            else:
                counter1 = 0
                won = False

            if board[j][i] == players[1]:
                counter2 = counter2 + 1
                if counter2 == 4:
                    print(f'{players[1]} is the winner')
                    won = True
                    return won
            else:
                counter2 = 0
                won = False

    # Diagonal
    counter1 = 0
    counter2 = 0
    for j in range(len(board[0])):
        if board[j][j] == players[0]:
            counter1 = counter1 + 1
            if counter1 == 4:
                print(f'{players[0]} is the winner')
                won = True
                return won
        else:
            counter1 = 0
            won = False

        if board[j][j] == players[1]:
            counter2 = counter2 + 1
            if counter2 == 4:
                print(f'{players[1]} is the winner')
                won = True
                return won
        else:
            counter2 = 0
            won = False

    for i in range(len(board[0])):
        i += 1
        counter1 = 0
        counter2 = 0
        for j in range(len(board[0])-1):
            if board[j][i] == players[0]:
                counter1 = counter1 + 1
                if counter1 == 4:
                    print(f'{players[0]} is the winner')
                    won = True
                    return won
            else:
                counter1 = 0
                won = False

            if board[j][i] == players[1]:
                counter2 = counter2 + 1
                if counter2 == 4:
                    print(f'{players[1]} is the winner')
                    won = True
                    return won
            else:
                counter2 = 0
                won = False
            i += 1
    return won


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
    board = np.zeros((7, 7), dtype=int)
    print(board)
    won = False
    players = [1, 2]
    player_cycle = itertools.cycle(players)
    while not won:
        current_player = next(player_cycle)
        played = False

        while not played:
            column_choice = int(input('Enter which column: '))
            played = fill_map(board, column_choice, current_player)
            print(board)

            if win(board, players, won):
                print(f'{current_player} won the game')
                return 0
            else:
                if np.count_nonzero(board) == board.size:
                    print('Match has been drawn')
                    if not won:
                        another_game()
                        return 0
                won = False


if __name__ == '__main__':
    main()