from typing import runtime_checkable
import random
player = "x"


#COORDINATES = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
coordinates_dict = {"A": 0, "B": 1, "C": 2}
#USED_COORDINATES = []


def init_board():
    board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    return board


def quit_game(user_input):
    if user_input.upper() == "QUIT":
        print("Goodbye")
        exit()


def validation_coordinate(used_coordinates, coordinates):
    while 1:
        user_input = (input("Get your coordinate: ")).upper()
        quit_game(user_input)
        if user_input in coordinates and user_input not in used_coordinates:
            used_coordinates.append(user_input)
            coordinates.remove(user_input)
            return user_input
        else:
            print("It's not valid coordinate, please try again")


def get_move(used_coordinates, coordinates):
    user_input = validation_coordinate(used_coordinates, coordinates)
    row = int(coordinates_dict[user_input[0]])
    col = int(user_input[1])
    return row, col-1


def get_ai_move(coordinates):
    bot_move = random.choice(coordinates)
    coordinates.remove(bot_move)
    row = int(coordinates_dict[bot_move[0]])
    col = int(bot_move[1])
    return row, col-1


def change_player(player):
    if player == "x":
        player = "o"
        return player
    if player == "o":
        player = "x"
        return player


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
        return True
    if player == board[0][0] and player == board[1][0] and player == board[2][0]:
        return True
    if player == board[0][0] and player == board[1][1] and player == board[2][2]:
        return True
    if player == board[0][1] and player == board[1][1] and player == board[2][1]:
        return True
    if player == board[0][2] and player == board[1][2] and player == board[2][2]:
        return True
    if player == board[0][2] and player == board[1][1] and player == board[2][0]:
        return True
    if player == board[1][0] and player == board[1][1] and player == board[1][2]:
        return True
    if player == board[2][0] and player == board[2][1] and player == board[2][2]:
        return True


def print_board(board):
    print(f"""         A   B   C
       1 {board[0][0]} | {board[0][1]} | {board[0][2]}  
         __|___|___
       2 {board[1][0]} | {board[1][1]} | {board[1][2]}  
         __|___|___
       3 {board[2][0]} | {board[2][1]} | {board[2][2]} """)


def print_result(board, player):
    has_won(board, player)


def tictactoe_game(board, player, used_coordinates, coordinates):
    print_board(board)
    while True:
        col, row = get_move(used_coordinates, coordinates)
        print(str(col), ' ', str(row))
        board = mark(board, player, row, col)
        board_full = is_full(board)
        if has_won(board, player) == True:
            print_board(board)
            print(f"Won Player: ", player)
            break
        elif board_full == True:
            print_board(board)
            print("It`s a Tie!")
            break
        player = change_player(player)
        print_board(board)


def tictactoe_game_vs_computer(board, player, random, used_coordinates, coordinates):
    print_board(board)
    while True:
        if player == 'x':
            col, row = get_ai_move(coordinates)
        elif player == 'o':
            col, row = get_move(used_coordinates, coordinates)
        print(str(col), ' ', str(row))
        board = mark(board, player, row, col)
        board_full = is_full(board)
        if has_won(board, player) == True:
            print_board(board)
            print(f"Won Player: ", player)
            break
        elif board_full == True:
            print_board(board)
            print("It`s a Tie!")
            break
        player = change_player(player)
        print_board(board)


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


def options(game_mode):
    if game_mode == 1:
        tictactoe_game(board, player, used_coordinates, coordinates)
    if game_mode == 2:
        tictactoe_game_vs_computer(
            board, player, random, used_coordinates, coordinates)


def main_menu():

    print('''Hello you are in the game which can destroy ur brain!
    You have 3 option to choose
    1. Player vs Player
    2. Player vs Computer
    3. Computer vs Computer
    Type "QUIT" to exit''')
    number = menu_valiadation()
    return number


if __name__ == '__main__':
    while True:
        game_mode = main_menu()
        board = init_board()
        used_coordinates = []
        coordinates = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        options(game_mode)
        print_board(board)
        answer = input("Do you want play again? Type 'n' if you wan`t! ")
        if answer.upper() == 'N':
            break
