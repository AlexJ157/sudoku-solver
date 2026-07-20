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
    
        
        

print_board(board)