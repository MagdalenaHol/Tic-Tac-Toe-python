from typing import runtime_checkable
import random


COORDINATES = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
COORDINATES_DICT = {"A": 0, "B": 1, "C": 2}
USED_COORDINATES = []


def init_board():  
    board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    print(f"""         A   B   C
       1 {board[0][0]} | {board[0][1]} | {board[0][2]}  
         __|___|___
       2 {board[1][0]} | {board[1][1]} | {board[1][2]}  
         __|___|___
       3 {board[2][0]} | {board[2][1]} | {board[2][2]} """)
    return board



def quit_game(user_input):
    if user_input == "QUIT":
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

#--------------------------------
# board = [[".", ".", "."], 
#          [".", ".", "."], 
#          [".", ".", "."]] 


# print(board) 
# print()


# player = "0"
# x = 0
# y = 2


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
    
    
# board = mark(board, player, x, y)


# player = "X"
# x = 2
# y = 1

# board = mark(board, player, 1, 1)
# board = mark(board, player, 1, 1)
# print(board)


def is_full(board):  
    for el_in_main_board in board:
        for el_in_inner_board in el_in_main_board:
            if el_in_inner_board == ".":
                return False
            
    return True
    

# board = [["x", "o", "o"], 
#          [".", "x", "."], 
#          ["o", ".", "x"]] 

# print(is_full(board))


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


# print(has_won(board, "o"))
# print(has_won(board, "x"))






def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    pass


def print_result(winner):  # Denys
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):  # Denys
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():  # Denys
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()










def main_menu():
    pass

"""    player mowe
    prawidłowy input
    u can`t input here!
    prawidwołe coordynate
    if true mark if false not mark or quit
    print mark on the board
    in row
    czy mozna zrobić jesze 1 ruch
    true == enother player mowe
    false == end game
    czy ktoś wygrał
1. def main_menu
2. Zaimplementować tablice init_board()
TTT = [["."]*3, ["."]*3, ["."]*3]
3. def whose_move()
random.choice(move)
4. def print_board(board)
board pojawia się przed każdym ruchem
5. Zaimplementować listę prawidłowych ruchów
6. def tictactoe_game():
    def get_move()
    - player X start the game
    - player move(ruch każdego gracza jest przechowywany)
    - player input(użyć try gdyby gracz wprowadził nieprawidłową wartość + ValueError by kontynuować,
                   walidacja czy prawidłowa pozycja gracza jest już zajęta)
    - jakiś update które miejsce na boardzie zajmuje player??

    def mark()
    - input playera(mark "X" or "O")

    def get_ai_move()

7. def has_won() sprawdzić czy ktoś wygrał
True or False:
    horizontal row winner
    vertical row winner
    diagonal row winner
8. def is_full()
9. def print_result()
-Congratulation! for the winner
-if moves == 9
print("Tie!")


1. def main_menu
2. Zaimplementować tablice init_board()
TTT = [["."]*3, ["."]*3, ["."]*3]
3. def whose_move()
random.choice(move)
4. def print_board(board)
board pojawia się przed każdym ruchem
5. Zaimplementować listę prawidłowych ruchów
6. def tictactoe_game():
    def get_move()
    - player X start the game
    - player move(ruch każdego gracza jest przechowywany)
    - player input(użyć try gdyby gracz wprowadził nieprawidłową wartość + ValueError by kontynuować,
                   walidacja czy prawidłowa pozycja gracza jest już zajęta)
    - jakiś update które miejsce na boardzie zajmuje player??

    def mark()
    - input playera(mark "X" or "O")

    def get_ai_move()

7. def has_won() sprawdzić czy ktoś wygrał
True or False:
    horizontal row winner
    vertical row winner
    diagonal row winner
8. def is_full()
9. def print_result()
-Congratulation! for the winner
-if moves == 9
print("Tie!")


--------------------------"""

#1. wyświetlanie menu
#2. menu_user_input (1,2,3)
#3. walidacja inputu 2. -> sprawdzenie czy wpisano 1,2,3 -> error i prośba o ponowny input (return 1,2,3,)
#4. create board return lista + print board
#5. prośba o koordynaty + user_coordinate_input 
#6. walidacja user_input - gdy nieprawidłowy input lub zajęte pole - prośba o ponowny coordinate_input x = return = [0[0]]
#7. zamiana elementu "." w liście na X, 0
"""TTT = ["X",".","."]
TTT = [1["."|"."|"."], 
         ___|___|___
       2["."|"."|"."], 
         ___|___|___
       3["."|"."|"."]]"""
       
#8. print listy
#9. walidacja wygranej return True, False
#10. walidacja remisu (czy jest miejsce na planszy) return True, False
#11. ruch drugiego gracza 5-10
