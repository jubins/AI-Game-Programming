# Tic-Tac-Toe Program

# importing all necessary libraries
import random
from time import sleep


# Creates an empty board
def create_board():
    return([[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]])


# Check for empty places on board
def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i, j))
    return l


# Select a random place for the player
def random_place(board, player):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    i, j = current_loc
    board[i][j] = player
    return board


# Checks whether the player has three
# of their marks in a horizontal row
def row_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x][y] != player:
                win = False
                continue
        if win is True:
            return win
    return win


# Checks whether the player has three
# of their marks in a vertical row
def col_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue
        if win is True:
            return win
    return win


# Checks whether the player has three
# of their marks in a diagonal row
def diag_win(board, player):
    win = True
    for x in range(len(board)):
        if board[x][x] != player:
            win = False
    return win


# Evaluates whether there is
# a winner or a tie
def evaluate(board, players):
    winner = 0
    for player in players:
        if (row_win(board, player) or
                col_win(board, player) or
                diag_win(board, player)):
            winner = player
    if any(0 not in b for b in board) and winner == 0:
        winner = -1
    return winner


# Validates human input if it is correct
def validate_human_input(current_loc, board):
    if ', ' in current_loc:
        current_loc = current_loc.split(', ')
    elif ',' in current_loc:
        current_loc = current_loc.split(',')
    else:
        return None
    if len(current_loc) > 4:
        return None
    i, j = current_loc[0], current_loc[1]
    if not i.isdigit() and not j.isdigit():
        return None
    i, j = int(i), int(j)
    if i > 8 or i < 0 or j > 8 or j < 0 or board[i][j] != 0:
        return None

    return i, j


def pprint(board):
    print('{}\n{}\n{}'.format(board[0], board[1], board[2]))


# Main function to start the game
def play_game():
    board, winner, counter = create_board(), 0, 1
    print('Empty Board:')
    pprint(board)
    human_player = input('Choose your player either X or O: ')
    if human_player == 'X':
        computer_player = 'O'
    elif human_player == 'O':
        computer_player = 'X'
    else:
        print('You choose invalid input so we will assign players.')
        computer_player = 'X'
        human_player = 'O'
    print("Human player: {}, Computer player: {}. Enter input (row, col) as board's location. Let's begin the game with Human!".format(human_player, computer_player))
    sleep(2)
    computer = 0
    human = 1

    while winner == 0:
        if human > 0:
            current_loc = input('\nHuman play: ')
            current_loc = validate_human_input(current_loc, board)
            if not current_loc:
                print('Invalid input! Please enter comma separated values between 0-2. For example: 0,0 or 1,0. We will play this turn on your behalf.')
                board = random_place(board, human_player)
            else:
                i, j = current_loc
                board[i][j] = human_player
            computer += 1
            human -= 1
        else:
            print('\nComputer play: ')
            board = random_place(board, computer_player)
            human += 1
            computer -= 1
        print("Board after " + str(counter) + " move")
        pprint(board)
        sleep(2)
        counter += 1
        winner = evaluate(board, [human_player, computer_player])
        if winner != 0:
            print()
            break
    return winner


# Driver Code
print("Winner is: " + str(play_game()))
