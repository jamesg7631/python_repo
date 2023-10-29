board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
# I think this is poorly designed. The reason is it returns True or False only after going through the full row/column
def row_winner(board):
    side = len(board)
    for i in range(side):
        count = 0
        for j in range(side):
            if board[i][0] == board[i][j]:
                count +=1
                if count == side:
                    return True
    else:
        return False
# I think this is poorly designed. The reason is it returns True or False only after going through the full row/column
def column_winner(board):
    side = len(board)
    for i in range(side):
        count = 0
        for j in range(side):
            if board[j][0] == board[j][i]:
                count += 1
                if count == side:
                    return True
    else:
        return False

def diagonal_winner(board):
    side = len(board)
    count = 0
    for i in range(side - 1):
        if(board[i][i] != board [i+1][i+1]):
            break
        else:
            count +=1
            if count == side:
                return True
    for i in range(side - 1):
        if(board[i][side - i - 1] != board[i+1][side - i - 2]):
            return False
    else:
        return True
        

# The funtion winner should use the funtions row_winner, column_winner and diagonal_winner
def winner(board):
    print("")

# Displays the current state of the game
def format_board(board):
    print()

# Takes user input to play a move
def play_move():
    print()

# function that puts it all together and runs the game interactively
def play_game(board):
    print()

