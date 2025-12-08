import numpy as np

# Read input from file 
with open("input.txt", "r") as f:
    lines = f.readlines()


cleaned_lines = []
for line in lines:
    vals = line.strip()
    cleaned_lines.append([x for x in vals])

arr = np.array(cleaned_lines)

curr_row = 0

split_at = []

def print_arr(a):
    for i in range(a.shape[0]):
        row_str = ""
        for j in range(a.shape[1]):
            row_str += a[i, j]
        print(row_str)

for row_idx in range(arr.shape[0]-1):
    if row_idx == 0:
        # this is the first row
        s_idx = None
        for j in range(arr.shape[1]):
            if arr[row_idx, j] == 'S':
                s_idx = j
                break
        # beneath S draw a |
        arr[row_idx+1, s_idx] = '|'
    else:
        for j in range(arr.shape[1]):
            val = arr[row_idx, j]
            if val == ".":
                continue

            val_below = arr[row_idx+1, j]
            if val == "|" and val_below == ".":
                # move down
                arr[row_idx+1, j] = "|"
            elif val == "|" and val_below == "^":
                # split
                split_at.append((row_idx, j))
                arr[row_idx+2, j-1] = "|"
                arr[row_idx+2, j+1] = "|"

    print("Step", row_idx)
    print_arr(arr)
    print()

print(len(set(split_at)))
# total = 0
# for j in range(len(cleaned_lines[0])):
#     operator = cleaned_lines[-1][j]
#
#     nums = []
#     for i in range(len(cleaned_lines)-1):
#         num = int(cleaned_lines[i][j])
#         nums.append(num)
#
#     value = None
#     for num in nums:
#         if value is None:
#             value = num
#         else:
#             if operator == '+':
#                 value += num
#             elif operator == '*':
#                 value *= num
#
#     print(value, nums)
#     total += value
# print(total)
#
#
#
