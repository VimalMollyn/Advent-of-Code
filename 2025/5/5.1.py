import numpy as np

# Read input from file 
with open("input.txt", "r") as f:
    lines = f.readlines()

ranges = []
ids = []
ranges_done = False

for line in lines:
    line = line.strip()
    if line == "":
        ranges_done = True
        continue
    if not ranges_done:
        start, end = line.split("-")
        start = int(start)
        end = int(end)
        ranges.append(range(start, end+1))
    else:
        ids.append(int(line))


total = 0
for i in ids:
    to_keep = False
    for r in ranges:
        if i in r:
            print(i)
            total += 1
            break

print("Total:", total)



