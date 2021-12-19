# --- Day 4: Giant Squid ---
# You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.
#
# Maybe it wants to play bingo?
#
# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)
#
# The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:
#
# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
#
# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19
#
#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6
#
# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7
# After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):
#
# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
# After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:
#
# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
# Finally, 24 is drawn:
#
# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
# At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).
#
# The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.
#
# To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

# input_text = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7"""

# import numpy
import numpy as np

# read the input from file
with open("input.txt") as f:
    input_text = f.read()

# function to parse the input
def parse_input(input_text):
    # first split the input into lines
    lines = input_text.split("\n")

    # the first line is the random drawn numbers of type int
    numbers = [int(x) for x in lines[0].split(",")]

    # the next lines are the boards
    # each board is separated by a blank line
    # if line is empty, we have reached the end of a board
    # each board is a 2d numpy array

    boards = []
    board = []
    for line in lines[1:]:
        # each board is a numpy array
        if line == "":
            # each board is of type int
            boards.append(np.array(board, dtype=int))
            board = []
        else:
            board.append(line.split())

    # append the last board
    boards.append(np.array(board, dtype=int))

    # remove empty boards
    boards = [board for board in boards if board.size > 0]

    return numbers, boards


# parse_input
numbers, boards = parse_input(input_text)

# create a list of empty boards of the same size as boards
# this will be used to store the marked numbers
marked_boards = [np.zeros(board.shape) for board in boards]

# init score to none
score = 0

# loop through each number in numbers
for number in numbers:
    # loop through each board in boards
    for i, board in enumerate(boards):
        # if the number is in the board, mark it in the marked_boards
        if number in board:
            marked_boards[i][board == number] = 1

        # check if any of the rows or columns in this board sum to the shape of the board
        # if so, we have a winner
        if np.any(np.sum(marked_boards[i], axis=0) == board.shape[0]) or np.any(
            np.sum(marked_boards[i], axis=1) == board.shape[1]
        ):
            # find the sum of the numbers in the board that are not marked
            unmarked_sum = np.sum(board[marked_boards[i] == 0])
            # multiply the sum by the number that was just called
            score = unmarked_sum * int(number)
            print("The score for board {} is {}".format(i, score))
            break

    # if we have a winner, break out of the loop
    if score > 0:
        break

# part 2

# init score to none
score = 0

# keep a track of the boards that have won
# this will be used to check if there are any boards that have not been won
boards_won = []

# loop through each number in numbers
for number in numbers:
    # loop through each board in boards
    for i, board in enumerate(boards):
        # check if the board has won already and if so, skip it
        if i in boards_won:
            continue

        # if the number is in the board, mark it in the marked_boards
        if number in board:
            marked_boards[i][board == number] = 1

        # check if any of the rows or columns in this board sum to the shape of the board
        # if so, we have a winner
        if np.any(np.sum(marked_boards[i], axis=0) == board.shape[0]) or np.any(
            np.sum(marked_boards[i], axis=1) == board.shape[1]
        ):
            # check if the number of boards that have won is equal to the number of boards - 1
            # if so, we have a winner
            if len(boards_won) == len(boards) - 1:
                # find the sum of the numbers in the board that are not marked
                unmarked_sum = np.sum(board[marked_boards[i] == 0])
                # multiply the sum by the number that was just called
                score = unmarked_sum * int(number)
                print("The score for board {} is {}".format(i, score))
                break
            else:
                # add the board to the list of boards that have won
                boards_won.append(i)

    # if we have a winner, break out of the loop
    if score > 0:
        break
