board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - -")
        for col in range(len(board[row])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")

            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")

def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return (row, col)
    return None

def valid(board, num, pos):
    # check row 
    for col in range(len(board)):
        if board[pos[0]][col] == num and pos[1] != col:
            return False
    
    # check col 
    for row in range(len(board)):
        if board[row][pos[1]] == num and pos[0] != row:
            return False

    # check square
    square_x = int(pos[0]/3)
    square_y = int(pos[1]/3)
    for row in range(square_x * 3, (square_x + 1) * 3):
        for col in range(square_y * 3, (square_y + 1) * 3):
            if board[row][col] == num and (pos[0] != row and pos[1] != col):
                return False
    return True

def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return (row, col)
    return None

def solve(board):
    empty = find_empty(board)
    if not empty: 
        return True
    else:
        row, col = empty
    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    
    return False

print_board(board)
print("-------------------------")
solve(board)
print_board(board)

