import numpy as np

# Read input from file 
with open("input.txt", "r") as f:
    lines = f.readlines()


cleaned_lines = []
for line in lines:
    vals = line.strip().split(' ')
    cleaned_lines.append([x for x in vals if x != ""])

total = 0
for j in range(len(cleaned_lines[0])):
    operator = cleaned_lines[-1][j]

    nums = []
    for i in range(len(cleaned_lines)-1):
        num = int(cleaned_lines[i][j])
        nums.append(num)

    value = None
    for num in nums:
        if value is None:
            value = num
        else:
            if operator == '+':
                value += num
            elif operator == '*':
                value *= num

    print(value, nums)
    total += value
print(total)



