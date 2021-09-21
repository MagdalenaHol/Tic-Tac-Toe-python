from typing import runtime_checkable


def init_board():  # Bartek
    """Returns an empty 3-by-3 board (with .)."""
    board = []
    return board


def get_move(board, player):  # Bartek
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def get_ai_move(board, player):  # Bartek
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):  # Magda
    """Marks the element at row & col on the board for player."""
    pass


def has_won(board, player):  # Magda
    """Returns True if player has won the game."""
    return False


def is_full(board):  # Magda
    """Returns True if board is full."""
    return False


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


def init_board():


def print_board(board):


def tictactoe_game(mode='HUMAN-HUMAN'):
    player mowe
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


--------------------------
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
