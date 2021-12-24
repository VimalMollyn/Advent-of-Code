from pathlib import Path
import numpy as np
from tqdm import trange

# set an imput file name
filename = Path("input.txt")

# read the file into a list of ints
with open(filename, "r") as f:
    int_list = [int(x) for x in f.read().split(",")]

# convert list to numpy array
int_array = np.array(int_list)

# create a variable to keep track of the number of days
day_count = 256

# loop through each day
print(f"Initial state: {int_array}")

# naive solution
# for day in trange(day_count):
#     # decrement all the numbers in the array
#     int_array -= 1
# 
#     # find all the -1s in the int array
#     indices = np.where(int_array == -1)
# 
#     # count the number of -1s
#     num_indices = len(indices[0])
# 
#     # set all the -1s to 6
#     int_array[indices] = 6
# 
#     # append the 8 number of -1s to the end of the array
#     int_array = np.append(int_array, np.zeros(num_indices) + 8)
# 
#     # print the state of the array
#     print(f"Day {day + 1}: {int_array}")
# 
# # count the number of elements in the array
# print("length of array:", len(int_array))


# better solution
# create a list that keeps track of the number of times each number from 0 to 8 appears
counts = [0] * 9

# fill the counts list with the number of times each number appears
for i in range(len(int_array)):
    counts[int_array[i]] += 1

# loop through the days
for day in trange(day_count):
    # left shift the counts list
    counts = np.roll(counts, -1)

    # add the number of the last element to the 7th element
    counts[6] += counts[-1]
    
    # print the current state of the counts int_list
    # print(f"Day {day + 1}: {counts}")

# print the answer
print(f"Answer: {sum(counts)}")

















