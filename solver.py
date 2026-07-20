import math

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_board(board):
    for row_index, row in enumerate(board):
        formatted_row = ""
        for value_index, value in enumerate(row):
            if value == 0:
                formatted_row += " "
            else:
                formatted_row += str(value)

            if (value_index + 1) % 3 == 0 and value_index != 8:
                formatted_row += "|"


        print(formatted_row)
        if (row_index + 1) % 3 == 0 and row_index != 8:
            print("---------")

def find_empty(board):
    for row_index, row in enumerate(board):
        for value_index, value in enumerate(row):
            if value == 0:
                return (row_index, value_index)
    return None
    
def is_valid(board, number, position):
    row, column = position
    for value in board[row]:
        if value == number:
            return False
        
    column_list = []
    for i in range(9):
        column_list.append(board[i][column])

    for value in column_list:
        if value == number:
            return False
        
    start_row = math.floor((row / 3)) * 3
    start_column = math.floor((column / 3)) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_column, start_column + 3):
            if board[i][j] == number:
                return False
    return True

def solve(board):
    empty_position = find_empty(board)
    if empty_position is None:
        print("Sudoku Solved")
        return True
    
    row, column = empty_position

    for number in range(1, 10):
        if is_valid(board, number, empty_position):
            board[row][column] = number
            
            if solve(board):
                return True
            board[row][column] = 0

    return False

print_board(board)
solve(board)
print_board(board)
print(solve(board))


