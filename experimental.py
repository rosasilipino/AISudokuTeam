import Sudoku
import time
import solver
import matplotlib.pyplot as plt


# Run this file to get information on how quickly things are running

def level1Test():

    experiment = []
    # Solve 100 boards of difficulty 1 and keep track of how long they take
    for i in range(1, 100):
        board = Sudoku.Board()
        board.Pick_Board(1)
        start_time = time.time()
        solver.Solve(board)
        end_time = time.time()
        experiment.append(end_time - start_time)

    # returns array with all the running times.
    return experiment


def level2Test():

    experiment = []
    # Solve 100 boards of difficulty 2 and keep track of how long they take
    for i in range(1,100):
        board = Sudoku.Board()
        board.Pick_Board(2)
        start_time = time.time()
        solver.Solve(board)
        end_time = time.time()
        experiment.append(end_time - start_time)

    # returns array with all the running times.
    return experiment

def level3Test():

    experiment = []
    # Solve 100 boards of difficulty 3 and keep track of how long they take
    for i in range(1,100):
        board = Sudoku.Board()
        board.Pick_Board(3)
        start_time = time.time()
        solver.Solve(board)
        end_time = time.time()
        experiment.append(end_time - start_time)

    # returns array with all the running times.
    return experiment


threeTests = [] # List that will get the avg completion times of the 3 difficulties

# Create a graph visualization of the running times for difficulty 1
solve_t1 = level1Test()
plt.figure(figsize=(10, 5))
plt.plot(solve_t1, marker='o')
plt.title('Sudoku Solve Times for 1 difficulty')
plt.xlabel('Trial')
plt.ylabel('Time in Seconds')
plt.grid(True)
plt.show()

average_time1 = sum(solve_t1) / len(solve_t1)
threeTests.append(average_time1) # append the avg time it took solve all 100 runs
print(f"The average solve time for level 1 is {average_time1:.3f} seconds.")

# Create a graph visualization of the running times for difficulty 2
solve_t2 = level2Test()
plt.figure(figsize=(10, 5))
plt.plot(solve_t2, marker='o')
plt.title('Sudoku Solve Times for 2 difficulty')
plt.xlabel('Trial')
plt.ylabel('Time in Seconds')
plt.grid(True)
plt.show()

average_time2 = sum(solve_t2) / len(solve_t2)
threeTests.append(average_time2) # append the avg time it took solve all 100 runs
print(f"The average solve time for level 2  is {average_time2:.3f} seconds.")


# Create a graph visualization of the running times for difficulty 1
solve_t3 = level3Test()
plt.figure(figsize=(10, 5))
plt.plot(solve_t3, marker='o')
plt.title('Sudoku Solve Times for 3 difficulty')
plt.xlabel('Trial')
plt.ylabel('Time in Seconds')
plt.grid(True)
plt.show()

average_time3 = sum(solve_t3) / len(solve_t3)
threeTests.append(average_time3) # append the avg time it took solve all 100 runs
print(f"The average solve time for level 3  is {average_time3:.3f} seconds.")

# Create a graph visualization of the avg running times for the 3 difficulties
plt.figure(figsize=(10, 5))
plt.plot(threeTests, marker='o')
plt.title('Avg Solve Times for the 3 difficulties')
plt.xlabel('Difficulty')
plt.ylabel('Time in Seconds')
plt.grid(True)
plt.show()



