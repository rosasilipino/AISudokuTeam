import pygame
from chooseLevel import *
import copy
import random
import solver
import time

pygame.init()

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


class Board:
    def __init__(self):
        self.board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
        self.initBoard = []

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
        level = chooseLevel()
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
    pygame.init()  # Initialize pygame here
    level = chooseLevel()  # Choose level
    if level == 1 or level == 2 or level == 3:
        print(f"Level {level} chosen.")
    elif not level:
        print("No level chosen, exiting...")
        pygame.quit()

    board = Board()
    board.Pick_Board(level)  # Pass level to this function instead of calling chooseLevel again inside

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Additional event handling here
        board.Draw()
       
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if not solver_triggered:  # This is here so that it doesn't print the timer multiple times
                solver_triggered = True  # Spacebar was pressed

                start_time = time.time()  # Start of timer
                solver.Solve(board)
                end_time = time.time()  # End of timer

                print(f"Sudoku solved in {end_time - start_time:.3f} seconds")
        else:
            solver_triggered = False  # Spacebar was not triggered

    pygame.quit()

if __name__ == '__main__':
    main()
