from typing import runtime_checkable
import random
current_player = "x"


COORDINATES = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
COORDINATES_DICT = {"A": 0, "B": 1, "C": 2}
USED_COORDINATES = []


def init_board():
    board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    return board


def quit_game(user_input):
    if user_input.upper() == "QUIT":
        print("Goodbye")
        exit()


def validation_coordinate(USED_COORDINATES, COORDINATES):
    while 1:
        user_input = (input("Get your coordinate: ")).upper()
        quit_game(user_input)
        if user_input in COORDINATES and user_input not in USED_COORDINATES:
            USED_COORDINATES.append(user_input)
            COORDINATES.remove(user_input)
            return user_input
        else:
            print("It's not valid coordinate, please try again")


def get_move(USED_COORDINATES, COORDINATES):
    user_input = validation_coordinate(USED_COORDINATES, COORDINATES)
    row = int(COORDINATES_DICT[user_input[0]])
    col = int(user_input[1])
    return row, col-1


def get_ai_move(COORDINATES):
    bot_move = random.choice(COORDINATES)
    COORDINATES.remove(bot_move)
    row = int(COORDINATES_DICT[bot_move[0]])
    col = int(bot_move[1])
    return row, col-1


get_ai_move(COORDINATES)

current_player = "x"


def change_player(current_player):
    if current_player == "x":
        current_player = "o"
    if current_player == "o":
        current_player = "x"
    return current_player


def mark(board, player, row, col):
    if row not in [0, 1, 2]:
        print("Row out- of bound")
        return board
    if col not in [0, 1, 2]:
        print("Col out- of bound")
        return board

    if board[row][col] != ".":
        print("It's occupied.")
        return board

    board[row][col] = player
    return board


def is_full(board):
    for el_in_main_board in board:
        for el_in_inner_board in el_in_main_board:
            if el_in_inner_board == ".":
                return False

    return True


def has_won(board, player):

    if player == board[0][0] and player == board[0][1] and player == board[0][2]:
        return "Won player: ", player
    if player == board[0][0] and player == board[1][0] and player == board[2][0]:
        return "Won player: ", player
    if player == board[0][0] and player == board[1][1] and player == board[2][2]:
        return "Won player: ", player
    if player == board[0][1] and player == board[1][1] and player == board[2][1]:
        return "Won player: ", player
    if player == board[0][2] and player == board[1][2] and player == board[2][2]:
        return "Won player: ", player
    if player == board[0][2] and player == board[1][1] and player == board[2][0]:
        return "Won player: ", player
    if player == board[1][0] and player == board[1][1] and player == board[1][2]:
        return "Won player: ", player
    if player == board[2][0] and player == board[2][1] and player == board[2][2]:
        return "Won player: ", player

    return False


def print_board(board):
    print(f"""         A   B   C
       1 {board[0][0]} | {board[0][1]} | {board[0][2]}  
         __|___|___
       2 {board[1][0]} | {board[1][1]} | {board[1][2]}  
         __|___|___
       3 {board[2][0]} | {board[2][1]} | {board[2][2]} """)


def print_result(board, player):
    has_won(board, player)


def tictactoe_game(board, player):
    current_player
    while True:
        print_board()
        get_move()
        mark()
        if has_won == True:
            break
        elif is_full() == True:
            break
        change_player()
    print(has_won(board, player))


def menu_valiadation():
    while 1:
        user_input = input()
        quit_game(user_input)
        try:
            numbers = int(user_input)
            if numbers == 1 or numbers == 2 or numbers == 3:
                return numbers
        except ValueError:
            print("Are you stupid? Pick 1,2 or 3 if you are not stupid!!!")


def main_menu():

    print('''Hello you are in the game which can destroy ur brain!
    You have 3 option to choose
    1. Player vs Player
    2. Player vs Computer
    3. Computer vs Computer
    Type "QUIT" to exit''')
    menu_valiadation()


if __name__ == '__main__':
    game_mode = main_menu()
    board = init_board()
    tictactoe_game(board)
