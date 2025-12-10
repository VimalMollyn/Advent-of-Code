# TOO SLOW
import numpy as np
import matplotlib.pyplot as plt

# Read input from file 
with open("input.txt", "r") as f:
    lines = f.readlines()

vectors = []
xs = []
ys = []
for line in lines:
    a, b = line.strip().split(",")
    a = int(a)
    b = int(b)
    vectors.append([a, b])
    xs.append(a)
    ys.append(b)

xs.append(vectors[0][0])
ys.append(vectors[0][1])

fig = plt.figure()
plt.plot(xs, ys)

from itertools import combinations
groups = combinations(vectors, 2)
print(f"Total groups: {len(list(combinations(vectors, 2)))}")

rects = []
for g in groups:
    a, b = g

    x1, y1 = a
    x2, y2 = b

    w = abs(x2 - x1) + 1
    h = abs(y2 - y1) + 1

    area = w * h
    rects.append([a, b, area])

# sort rects by area
rects = sorted(rects, key=lambda x: x[2], reverse=True)

line_segments = [(vectors[i], vectors[(i+1)%len(vectors)]) for i in range(len(vectors))]
print(len(line_segments))
print(len(rects))
candidate = None
for rect in rects:
    a, b = rect[0], rect[1]
    min_x = min(a[0], b[0])
    max_x = max(a[0], b[0])
    min_y = min(a[1], b[1])
    max_y = max(a[1], b[1])
    if rect[2] == 0:
        continue
    # check if valid, it should not intersect with any vectors
    intersects = False
    for l in line_segments:
        # check if the l intersects with the rectangle formed by a and b
        (x1, y1), (x2, y2) = l

        # if line is vertical
        if x1 == x2:
            # check if the x coordinate of the line is between the x coordinates of a and b
            x = x1
            y_min = min(y1, y2)
            y_max = max(y1, y2)
            if min_x < x < max_x and max(y_min, min_y) < min(y_max, max_y):
                intersects = True
                break

        # if line is horizontal
        elif y1 == y2:
            y = y1
            x_min = min(x1, x2)
            x_max = max(x1, x2)
            if min_y < y < max_y and max(x_min, min_x) < min(x_max, max_x):
                intersects = True
                break

    if not intersects:
        candidate = rect
        print(f"Found rectangle between {a} and {b} with area {rect[2]}")
        break


# plot the rectangle
if candidate:
    a, b = candidate[0], candidate[1]
    plt.scatter([a[0], b[0]], [a[1], b[1]], color='red')

plt.show()
