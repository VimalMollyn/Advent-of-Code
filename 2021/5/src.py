# --- Day 5: Hydrothermal Venture ---
# You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.
#
# They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:
#
# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2
# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:
#
# An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
# An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
# For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.
#
# So, the horizontal and vertical lines from the above list would produce the following diagram:
#
# .......1..
# ..1....1..
# ..1....1..
# .......1..
# .112111211
# ..........
# ..........
# ..........
# ..........
# 222111....
# In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.
#
# To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.
#
# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

# set a filename to read from
from collections import defaultdict


filename = "input.txt"

# read the file
with open(filename) as f:
    content = f.readlines()

# parse the content
# the file contains pairs of coordinates
# the points are separated by a ->
# the coordinates are separated by a comma

# create a dict for each point to keep track of the number of lines it is covered by
# the dict will have the form {(x,y): num_lines}
# make this a defaultdict with a default value of 0
# the default value is used to keep track of the number of lines that overlap

points = defaultdict(int)

for line in content:
    # split the line into two coordinates
    coords = line.split("->")

    # split the coordinates into two points
    # the points are separated by a comma
    # the points are in the format x,y
    # so we split on the comma
    # and then split on the comma again
    # to get the x and y values
    # and then convert the string to an int
    # and then convert the x and y values to integers
    # and then store them in a tuple
    point1 = tuple(map(int, coords[0].split(",")))
    point2 = tuple(map(int, coords[1].split(",")))

    # if line is horizontal
    if point1[0] == point2[0]:
        # iterate through the y values
        # and add the line to the dict
        for y in range(min(point1[1], point2[1]), max(point1[1], point2[1]) + 1):
            points[(point1[0], y)] += 1

    # if line is vertical
    elif point1[1] == point2[1]:
        # iterate through the x values
        # and add the line to the dict
        for x in range(min(point1[0], point2[0]), max(point1[0], point2[0]) + 1):
            points[(x, point1[1])] += 1

    # if line is neither horizontal nor vertical
    else:
        # skip this line
        continue


# iterate through the points
# and count the number of lines that overlap with at least 2 points
num_overlaps = 0
for point in points:
    if points[point] >= 2:
        num_overlaps += 1

# print the number of overlaps
print(num_overlaps)

# part 2
# --- Part Two ---

points = defaultdict(int)

for line in content:
    # split the line into two coordinates
    coords = line.split("->")

    # split the coordinates into two points
    # the points are separated by a comma
    # the points are in the format x,y
    # so we split on the comma
    # and then split on the comma again
    # to get the x and y values
    # and then convert the string to an int
    # and then convert the x and y values to integers
    # and then store them in a tuple
    point1 = tuple(map(int, coords[0].split(",")))
    point2 = tuple(map(int, coords[1].split(",")))

    # if line is horizontal
    if point1[0] == point2[0]:
        # iterate through the y values
        # and add the line to the dict
        for y in range(min(point1[1], point2[1]), max(point1[1], point2[1]) + 1):
            points[(point1[0], y)] += 1

    # if line is vertical
    elif point1[1] == point2[1]:
        # iterate through the x values
        # and add the line to the dict
        for x in range(min(point1[0], point2[0]), max(point1[0], point2[0]) + 1):
            points[(x, point1[1])] += 1

    # if the line is diagonal at 45 degrees
    elif abs(point1[0] - point2[0]) == abs(point1[1] - point2[1]):
        # find the sign of the slope of the line
        # if the slope is positive, the line is going up
        # if the slope is negative, the line is going down
        # find the x slope and y slope
        x_slope_sign = 1 if point2[0] - point1[0] > 0 else -1
        y_slope_sign = 1 if point2[1] - point1[1] > 0 else -1

        # travel from point1 to point2
        # and add the line to the dict
        for x, y in zip(
            range(point1[0], point2[0] + x_slope_sign, x_slope_sign),
            range(point1[1], point2[1] + y_slope_sign, y_slope_sign),
        ):
            points[(x, y)] += 1

    # if line is neither horizontal nor vertical
    else:
        # skip this line
        continue

# iterate through the points
# and count the number of lines that overlap with at least 2 points
num_overlaps = 0
for point in points:
    if points[point] >= 2:
        num_overlaps += 1

# print the number of overlaps
print(num_overlaps)
