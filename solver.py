def Solve(board):
    board.Draw()
    find = Find_Empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if Valid(board, i, (row, col)):
            board.Get_Board()[row][col] = i

            if Solve(board):
                return True

            board.Get_Board()[row][col] = 0

    return False


def Find_Empty(board):
    for i in range(9):
        for j in range(9):
            if board.Get_Board()[i][j] == 0:
                return [i, j]  # row, col

    return None


def Valid(board, num, pos):
    # Check row
    for i in range(9):
        if board.Get_Board()[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if board.Get_Board()[i][pos[1]] == num and pos[0] != i:
            return False

    # Check boardx
    boardx_x = pos[1] // 3
    boardx_y = pos[0] // 3

    for i in range(boardx_y * 3, boardx_y * 3 + 3):
        for j in range(boardx_x * 3, boardx_x * 3 + 3):
            if board.Get_Board()[i][j] == num and (i, j) != pos:
                return False

    return True

