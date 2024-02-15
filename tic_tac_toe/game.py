import random


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
separator = ("=" * 40)


def welcome() -> None:
    """
    This function welcomes the user and introduces the rules of the game Tic Tac Toe.
    """
    
    print("Welcome to Tic Tac Toe")
    print(separator)
    print("""
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
    """
)
    print(separator)
    print("Let's start the game")
    print("-" * 40)
    
    
def print_board(board) -> None:
    """
    This function prints a board
    """
    print("----------")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("----------")
    print(separator)
    
    
def choose_symbol() -> None:
    """
    This function wants players to choose symbols to play
    """
    
    while True:
        symbol_1 = input("Player 1, do you wnat to be 'X' or 'O'? \n").upper()
        if symbol_1 not in ["X", "O"]:
            print("Invalid input. Please enter X or O.")
            
        if symbol_1 == "X":
            symbol_2 = "O"
            print("Player 1 you're 'X'.")
            print("Player 2 you're 'O'.")
            break
        else:
            symbol_2 = "X"
            print("Player 1 you're '0'.")
            print("Player 2 you're 'X'.")
            break
    return symbol_1, symbol_2


def placement(symbol_1, symbol_2) -> None:
    current_player = 1
    
    while True:
        if current_player == 1:
            position = input(f"Player {current_player} enter your move number (1-9): ")
            if not position.isnumeric():
                print("Enter a number!")
                continue
            
            position = int(position)
            if position > 9 or position < 1:
                print("Enter a number between 1 and 9!")
                continue
            elif board[position -1] != "-":
                print("Position is taken.")   
                continue
        else:
            position = random.randint(1, 9)
            if board[position -1] != "-":
                continue
        
        if current_player == 1:
            board[position -1] = symbol_1
        else:
            board[position -1] = symbol_2
            
        print_board(board)
        
        current_player = 2 if current_player == 1 else 1
        
        if win(board, symbol_1, symbol_2):
            break


def win(board, symbol_1, symbol_2):
    wins = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]
    
    for combo in wins:
        if combo == [symbol_1, symbol_1, symbol_1]:
            print(f"Congratulations, the player with symbol {symbol_1} won!")
            return
        elif combo == [symbol_2, symbol_2, symbol_2]:
            print(f"Congratulations, the player with symbol {symbol_2} won!")
            return
        if "-" not in board:
            print("It's a draw!")
            return
    
    
    
def game():
    welcome()
    print_board(board)
    symbol_1, symbol_2 = choose_symbol()
    placement(symbol_1,symbol_2)
    

if __name__ == "__main__":
    game()