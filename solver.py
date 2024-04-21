def Solve(board):
    empty = Find_Empty(board)
    if not empty:
        return True  # No empty cell found, puzzle is solved
    row, col = empty

    for value in Get_Possible_Values(board, (row, col)):
        board.Get_Board()[row][col] = value
        if Solve(board):
            return True
        board.Get_Board()[row][col] = 0  # Backtrack if solution path fails

    return False  # Trigger backtracking


def Find_Empty(board):
    min_remaining_values = float('inf')
    next_cell = None
    for i in range(9):
        for j in range(9):
            if board.Get_Board()[i][j] == 0:
                remaining_values = len(Get_Possible_Values(board, (i, j)))
                if remaining_values < min_remaining_values:
                    min_remaining_values = remaining_values
                    next_cell = [i, j]
    return next_cell


# ADDED
def Get_Possible_Values(board, pos):
    row, col = pos
    possible_values = set(range(1, 10))  # Start with all possible values from 1 to 9

    # Eliminate values based on the row
    possible_values -= set(board.Get_Board()[row])

    # Eliminate values based on the column
    possible_values -= set(board.Get_Board()[i][col] for i in range(9))

    # Eliminate values based on the 3x3 box
    box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            possible_values.discard(board.Get_Board()[i][j])

    return list(possible_values)


def Valid(board, num, pos):
    # Check row
    for i in range(9):
        if board.Get_Board()[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if board.Get_Board()[i][pos[1]] == num and pos[0] != i:
            return False

    # Check board
    boardx_x = pos[1] // 3
    boardx_y = pos[0] // 3

    for i in range(boardx_y * 3, boardx_y * 3 + 3):
        for j in range(boardx_x * 3, boardx_x * 3 + 3):
            if board.Get_Board()[i][j] == num and (i, j) != pos:
                return False

    return True