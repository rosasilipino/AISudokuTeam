import Sudoku
import time
import solver
import matplotlib.pyplot as plt


# Run this file to get information on how quckly things are running

def level1Test():

    experiment = []
    for i in range(1,100):
        board = Sudoku.Board()
        board.Pick_Board(1)
        start_time = time.time()
        solver.Solve(board)
        end_time = time.time()
        experiment.append(end_time - start_time)

    return experiment


def level2Test():

    experiment = []
    for i in range(1,100):
        board = Sudoku.Board()
        board.Pick_Board(2)
        start_time = time.time()
        solver.Solve(board)
        end_time = time.time()
        experiment.append(end_time - start_time)

    return experiment

def level2Test():

    experiment = []
    for i in range(1,100):
        board = Sudoku.Board()
        board.Pick_Board(3)
        start_time = time.time()
        solver.Solve(board)
        end_time = time.time()
        experiment.append(end_time - start_time)

    return experiment



solve_t1 = level1Test()
plt.figure(figsize=(10, 5))
plt.plot(solve_t1, marker='o')
plt.title('Sudoku Solve Times')
plt.xlabel('Trial')
plt.ylabel('Time in Seconds')
plt.grid(True)
plt.show()
