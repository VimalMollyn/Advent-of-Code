import numpy as np

# Read input from file 
with open("input.txt", "r") as f:
    lines = f.readlines()

arr = np.zeros((len(lines), len(lines[0].strip()))).astype(int)
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '@':
            arr[i][j] = 1

def count_neighbors(x, y):
    count = 0
    min_x = max(0, x - 1)
    max_x = min(arr.shape[0] - 1, x + 1)
    min_y = max(0, y - 1)
    max_y = min(arr.shape[1] - 1, y + 1)

    neighbor_grid = arr[min_x:max_x + 1, min_y:max_y + 1]
    total = np.sum(neighbor_grid) - 1
    return total

total_list = []
while True:
    total = 0
    to_update = []
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i][j] == 1:
                neighbors = count_neighbors(i, j)
                if neighbors < 4:
                    total += 1
                    to_update.append((i, j))
    print(total)
    total_list.append(total)

    # update the array replace 1 with 0 for the positions in to_update
    for pos in to_update:
        arr[pos[0]][pos[1]] = 0

    if total == 0:
        break

print(f"total total: {sum(total_list)}")
