#Group: Sudoku Team
#Class: CS 450-01
#Project: Final Project
#Date: 04/21/2024

from turtle import Screen
from chooseLevel import *
from runIterations import *
import copy
import random
import solver
import time

pygame.init()

# Intialize the window
WIN_WIDTH = 700
SCALE = WIN_WIDTH // 9
WIN_HEIGHT = WIN_WIDTH + SCALE//2
WINDOW = pygame.display.set_mode((WIN_WIDTH, int(WIN_HEIGHT)))
pygame.display.set_caption("CS450 SUDOKU TEAM")
STAT_FONT = pygame.font.SysFont("freesansbold", int(SCALE//1.3))
LABEL_FONT = pygame.font.SysFont("freesansbod", int(SCALE//2.8))

# Color Pallet
BLACK = [72, 72, 72]
GREY = [200, 200, 200]
TEXT = [160, 160, 160]
ITEXT = [153, 102, 51]
WHITE = [255, 255, 255]

# Class to create the board
class Board:
    def __init__(self):
        # Initialize a new board as a 9x9 grid filled with zeros
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.initBoard = []
        
    def resetBoard(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def findEmpty(firstBoard):
        for y in range(len(firstBoard)):
            for x in range(len(firstBoard[0])):
                if firstBoard[y][x] == 0:
                    return y, x  # y = row , x = column
        # if we got here it mean that we finish the sudoku, so return none
        return None

    def validCheck(firstBoard, number, coordinates):
        # checking row
        for x in range(len(firstBoard[0])):
            if number == firstBoard[coordinates[0]][x] and coordinates[1] != x:  # coordinates[0]= row
                return False

        # checking column
        for y in range(len(firstBoard)):
            if number == firstBoard[y][coordinates[1]] and coordinates[0] != y:
                return False

        # checking the box
        box_x = coordinates[1] // 3
        box_y = coordinates[0] // 3

        for y in range(box_y * 3, box_y * 3 + 3):
            for x in range(box_x * 3, box_x * 3 + 3):
                if number == firstBoard[y][x] and (y, x) != coordinates:
                    return False
        return True

    def generateRandomBoard(firstBoard):
        # end condition:- getting to the end of the board - the function findEmpty return NONE
        find = Board.findEmpty(firstBoard)
        if find is None:  # if find != False
            return True
        else:
            row, col = find
        for number in range(1, 10):
            randomNumber = random.randint(1, 9)
            if Board.validCheck(firstBoard, randomNumber, (row, col)):
                firstBoard[row][col] = randomNumber
                if Board.generateRandomBoard(firstBoard):
                    return True
                firstBoard[row][col] = 0
        return False

    # Delete cells from the board to make it a puzzle.
    def deleteCells(firstBoard, number):
        while number:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if firstBoard[row][col] != 0:
                firstBoard[row][col] = 0
                number = number - 1

    def sudokuGenerate(firstBoard, level):
        # printBoard(firstBoard)
        Board.generateRandomBoard(firstBoard)
        # printBoard(firstBoard)
        if level == 1:
            Board.deleteCells(firstBoard, 30)
        if level == 2:
            Board.deleteCells(firstBoard, 40)
        if level == 3:
            Board.deleteCells(firstBoard, 50)
        
    def Pick_Board(self, level):
        Board.sudokuGenerate(self.board, level)

    def Get_Board(self):
        return self.board

    def Draw(self):
        WINDOW.fill(WHITE)
        for x in range(0, WIN_WIDTH, SCALE):
            pygame.draw.line(WINDOW, GREY, (x, 0), (x, WIN_WIDTH), 4)
            pygame.draw.line(WINDOW, GREY, (0, x), (WIN_WIDTH, x), 4)

        for x in range(0, WIN_WIDTH + 1, WIN_WIDTH // 3 - 1):
            pygame.draw.line(WINDOW, BLACK, (x, 0), (x, WIN_WIDTH), 8)
            pygame.draw.line(WINDOW, BLACK, (0, x), (WIN_WIDTH, x), 8)

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                text = STAT_FONT.render("{}".format(self.board[row][col] if self.board[row][col] > 0 else ""), 1, TEXT)
                Wgap = (SCALE - text.get_width()) // 2
                Hgap = (SCALE - text.get_height()) // 2
                WINDOW.blit(text, (col * SCALE + Wgap + 2, row * SCALE + Hgap+3))

        for row in range(len(self.initBoard)):
            for col in range(len(self.initBoard[row])):
                text = STAT_FONT.render("{}".format(self.initBoard[row][col] if self.initBoard[row][col] > 0 else ""), 1, ITEXT)
                Wgap = (SCALE - text.get_width()) // 2
                Hgap = (SCALE - text.get_height()) // 2
                WINDOW.blit(text, (col * SCALE + Wgap + 2, row * SCALE + Hgap+3))

        text = LABEL_FONT.render("{}".format("PRESS SPACE TO SOLVE AUTOMATICALLY."), 1, BLACK)
        WINDOW.blit(text, (int(WIN_WIDTH//2 - text.get_width()//2), int(WIN_HEIGHT-SCALE//2.7)))

        pygame.display.update()

# Updated main function to utilize level chosen from chooseLevel.py - ROSE
def main():
    pygame.init()
    
    WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    
    # Level selection section.
    level = chooseLevel(WINDOW)  # Choose level
    if level not in [1, 2, 3]:
        print("NO LEVEL WAS CHOSEN. EXITING PROGRAM.")
        pygame.quit()
    
    # Number of puzzles to solve section.
    numPuzzles = getNumOfRuns(WINDOW, "ENTER A NUMBER OF PUZZLES TO SOLVE: ")  # Get number of runs
    try:
        numPuzzles = int(numPuzzles)  # Convert to int
    except ValueError:
        print("ERROR: INVALID INPUT, SETTING NUMBER OF PUZZLES TO SOLVE TO 1.")
        numPuzzles = 1
    print(f"LEVEL {level} WAS CHOSEN. SOLVING {numPuzzles} LEVEL {level} PUZZLES.")
    board = Board()
    
    space_allowed = True # Controls when space bar is allowed.
    # Loop to generate and solve puzzles.
    for _ in range(numPuzzles):
        board.Pick_Board(level)
        board.Draw()
        pygame.display.update()
        
        # Print unsolved board state
        print("Unsolved board state:")
        for row in board.Get_Board():
            print(row)
        
        solved = False
        while not solved:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If the user closes the window, exit the game loop
                    print("EXITING PROGRAM X WAS PRESSED.")
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP: # If the user presses a key
                    if event.key == pygame.K_ESCAPE: # If user presses escape, exit the game loop
                        print("EXITING PROGRAM ESC WAS PRESSED.")
                        pygame.quit()
                        sys.exit()
                    if space_allowed: # If space is allowed
                        if event.key == pygame.K_SPACE:# If user presses space.
                            start_time = time.time() # Start timer
                            solver.Solve(board)
                            board.Draw()
                            #pygame.display.update()
                            end_time = time.time() #End timer
                            
                            # Print solved board state.
                            print("SUCCESS: SOLVED BOARD")
                            print("Board state after solve:")
                            for row in board.Get_Board():
                                print(row)
                            print(f"SUDOKU SOLVED IN {end_time - start_time:.3f} SECONDS.\n")
                            
                            time.sleep(3)  # Delay for 3 seconds to see the solved board
                            solved = True 
    pygame.quit()

if __name__ == '__main__':
    main()