import numpy as np

# Read input from file 
with open("input.txt", "r") as f:
    lines = f.readlines()

total_joltage = 0
for line in lines:
    line = line.strip()

    digits = []
    start = 0
    for i in range(12):
        end = -(12 - i) + 1
        if end == 0:
            end = len(line)
        searchable_line = line[start:end]
        # print(f"Searching in: {searchable_line}")
        index = np.argmax(np.array([int(x) for x in searchable_line]))
        # print(f"Found index: {index}, digit: {searchable_line[index]}")
        start += index + 1
        digits.append(searchable_line[index])

    best = int("".join(digits))
    # print(best)
    total_joltage += best
print(total_joltage)


