#Suduko Solver
import numpy as np

def is_valid(board, row, col, num):
    # Check if 'num' is not in the current row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if 'num' is not in the current column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if 'num' is not in the current 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(board):
    # Find the next empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True



print("Enter the initial sudoku (with blank places represented by 0): ")
sudoku = []
for i in range(9):
    row = list(map(int, input(f"Enter row {i+1}: ")))
    sudoku.append(row)
print(np.matrix(sudoku))
if solve_sudoku(sudoku):
    print("Sudoku has been successfully solved!")
    print(np.matrix(sudoku))

