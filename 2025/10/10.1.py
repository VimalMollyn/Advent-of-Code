import numpy as np
from itertools import combinations

# Read input from file 
with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0
for line in lines:
    # [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    line = line.strip()
    parts = line.split(" ")

    pattern = parts[0].strip("[]")
    buttons = parts[1:-1]

    # convert to binary
    binary_pattern = pattern.replace(".", "0").replace("#", "1")
    pattern_length = len(binary_pattern)

    # convert buttons to binary
    binary_buttons = []
    for button in buttons:
        b = [0] * pattern_length
        button_ids = button.strip("()").split(",")
        for idx in button_ids:
            b[int(idx)] = 1

        binary_buttons.append("".join([str(x) for x in b]))

    # print(binary_buttons)
    # print(binary_pattern)

    # get all combinations of binary_buttons
    found = False
    for r in range(1, len(binary_buttons) + 1):
        for combo in combinations(binary_buttons, r):
            # print(combo)

            # xor the combos
            xor_result = int(combo[0], 2)
            for b in combo[1:]:
                xor_result ^= int(b, 2)

            # check if xor_result matches binary_pattern
            if xor_result == int(binary_pattern, 2):
                print("Found combination:", combo, "r", r)
                total += r
                found = True
                break
        if found:
            break

print("Total:", total)
