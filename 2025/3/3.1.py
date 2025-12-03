# Read input from file 
with open("input.txt", "r") as f:
    lines = f.readlines()

total_joltage = 0
for line in lines:
    line = line.strip()
    best = 0
    for i, char in enumerate(line[:-1]):
        second_digit = str(max([int(x) for x in line[i+1:]]))
        candidate = int(f"{char}{second_digit}")
        if candidate > best:
            best = candidate

    print(best)
    total_joltage += best
print(total_joltage)


