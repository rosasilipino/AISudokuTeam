import os
import copy

from Sudoku import SudokuPuzzleGenerator

CLEAR = 'cls' # For linux or mac, replace 'cls' with 'clear'

# Global variable to keep track of possibilities for each cell
possibilities = [[list(range(1, 10)) for _ in range(9)] for _ in range(9)]


generator = SudokuPuzzleGenerator(num_holes=40)
puzzle, solution = generator.generate_puzzle()

sudoku = []
row = []

sudoku = copy.deepcopy(puzzle)

def solve(board):
    # Find the empty cell with the fewest possibilities
    find = find_best_empty_cell(board)
    if not find:
        return True
    else:
        row, col = find

    # Try numbers from 1 to 9
    for i in range(1,10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            os.system(CLEAR)        #Comment this line if you don't want to see the solution to increase the speed
            print("\nSolution: \n") #Comment this line if you don't want to see the solution to increase the speed
            print_sudoku(sudoku)    #Comment this line if you don't want to see the solution to increase the speed

            # Propagate constraints
            update_possibilities(board, i, (row, col))

            if solve(board):
                return True

            # Undo move and backtrack
            board[row][col] = 0
            restore_possibilities(board, i, (row, col))

    return False

def is_valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    boardx_x = pos[1] // 3
    boardx_y = pos[0] // 3

    for i in range(boardx_y*3, boardx_y*3 + 3):
        for j in range(boardx_x * 3, boardx_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def print_sudoku(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("------+-------+-------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                if board[i][j] == 0:
                    print(" ")
                else:
                    print(board[i][j])
            else:
                if board[i][j] == 0:
                    print(" " + " ", end="")
                else:
                    print(str(board[i][j]) + " ", end="")


def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None

def find_best_empty_cell(board):
    min_possibilities = 10  # More than the maximum number of possibilities
    best_cell = None
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0 and len(possibilities[i][j]) < min_possibilities:
                min_possibilities = len(possibilities[i][j])
                best_cell = (i, j)
    return best_cell

def update_possibilities(board, num, pos):
    # Remove num from possibilities for all cells in the same row, column, and block
    for i in range(9):
        if num in possibilities[i][pos[1]]:
            possibilities[i][pos[1]].remove(num)
        if num in possibilities[pos[0]][i]:
            possibilities[pos[0]][i].remove(num)
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if num in possibilities[i][j]:
                possibilities[i][j].remove(num)

def restore_possibilities(board, num, pos):
    # Add num back to possibilities for all cells in the same row, column, and block
    for i in range(9):
        if board[i][pos[1]] == 0 and num not in possibilities[i][pos[1]]:
            possibilities[i][pos[1]].append(num)
        if board[pos[0]][i] == 0 and num not in possibilities[pos[0]][i]:
            possibilities[pos[0]][i].append(num)
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == 0 and num not in possibilities[i][j]:
                possibilities[i][j].append(num)

os.system(CLEAR)
print("\nProblem: \n")
print_sudoku(sudoku) # Unsolved

input("\nPress Enter to See the Solution...")
solve(sudoku)

mySolution = []
for i in range(9):
    row = []
    for j in range(9):
        row.append(sudoku[i][j])
    mySolution.append(row)

os.system(CLEAR)
print("\nSolution\n")
print_sudoku(solution)
print("\nThe solution is verified\n")
print_sudoku(sudoku)
