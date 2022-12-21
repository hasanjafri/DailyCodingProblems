def sudoku_solver(board):
    # Find an empty cell
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                # Try every number from 1 to 9 as a possibility
                for k in range(1, 10):
                    if is_valid(board, i, j, k):
                        # If the number is valid, place it and recursively try to solve the rest of the board
                        board[i][j] = k
                        if sudoku_solver(board):
                            return True
                        # If the recursive call returns False, it means the placement was not valid, so we reset the cell to 0 and try the next possibility
                        board[i][j] = 0
                # If none of the numbers from 1 to 9 were valid, return False to trigger backtracking
                return False
    # If the board is full and all placements are valid, return True
    return True


def is_valid(board, row, col, num):
    # Check if the number is already in the row
    if num in board[row]:
        return False
    # Check if the number is already in the column
    for i in range(9):
        if board[i][col] == num:
            return False
    # Check if the number is already in the 3x3 box
    box_row = row // 3
    box_col = col // 3
    for i in range(3):
        for j in range(3):
            if board[box_row*3 + i][box_col*3 + j] == num:
                return False
    # If the number is not in the row, column, or box, it is valid
    return True


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

if __name__ == '__main__':
    print('Before:')
    print(board)
    sudoku_solver(board)
    print('After:')
    print(board)
