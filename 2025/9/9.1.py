import numpy as np

# Read input from file 
with open("input.txt", "r") as f:
    lines = f.readlines()

vectors = []
for line in lines:
    vectors.append(line.strip())

# get all groups of 2 vectors
from itertools import combinations

groups = combinations(vectors, 2)
print(f"Total groups: {len(list(combinations(vectors, 2)))}")

max_area = 0
for g in groups:
    a, b = g

    x1, y1 = map(int, a.split(","))
    x2, y2 = map(int, b.split(","))

    w = abs(x2 - x1) + 1
    h = abs(y2 - y1) + 1

    area = w * h
    print(f"Area between {a} and {b}: {area}")
    if area > max_area:
        max_area = area
print(max_area)
