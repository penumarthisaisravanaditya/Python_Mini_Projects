# Tic Tac Toe Game

board = [" " for i in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()
    
def check_winner(player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for position in winning_combinations:
        if all(board[i] == player for i in position):
            return True
    return False

def check_draw():
    return " " not in board

#Game Starts

print("Welcome to Tic Tac Toe!")
print("Positions are numbered as follows:")
print(" 1 | 2 | 3 ")
print("-----------")
print(" 4 | 5 | 6 ")
print("-----------")
print(" 7 | 8 | 9 ")

current_player = "X"

while True:
    
    print_board()
    
    try:
        position = int(input(f"Player {current_player}, enter your position (1-9): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")
        continue
    
    if position < 1 or position > 9:
        print("Invalid position. Please enter a number between 1 and 9.")
        continue
    
    position-=1
    
    if board[position] != " ":
        print("Position already taken. Please choose another position.")
        continue
    board[position] = current_player
    
    if check_winner(current_player):
        print_board()
        print(f"🎉🎉Player {current_player} wins!")
        break
    if check_draw():
        print_board()
        print("It's a draw!")
        break
    
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"