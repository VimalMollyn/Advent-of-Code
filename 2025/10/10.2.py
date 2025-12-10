import numpy as np
from z3 import *

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
    joltage = [int(x) for x in parts[-1].strip("{}").split(",")]

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

        binary_buttons.append(b)

    print(binary_buttons)
    print(binary_pattern)
    print(joltage)

    # Example data
    bitstrings = binary_buttons
    target = joltage

    # bitstrings as digit vectors
    values = binary_buttons 

    target = joltage

    n = len(values)        # number of vectors
    d = len(target)        # number of digits

    opt = Optimize()

    # integer weights >= 0
    weights = [Int(f"w{i}") for i in range(n)]
    for w in weights:
        opt.add(w >= 0)

    # digit-wise constraints: sum_i (w_i * v_i[j]) == target[j]
    for j in range(d):
        opt.add(sum(weights[i] * values[i][j] for i in range(n)) == target[j])

    # minimize total weight
    total_weight = sum(weights)
    opt.minimize(total_weight)

    if opt.check() == sat:
        m = opt.model()
        print("Solution:")
        for i in range(n):
            print("value:", values[i], "weight:", m[weights[i]])
        total_weight = m.evaluate(total_weight)
        print("Total weight:", total_weight)
        total += total_weight.as_long()
    else:
        print("No solution")
print("Total:", total)
