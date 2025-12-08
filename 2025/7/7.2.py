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

# split_at = []

def print_arr(a):
    for i in range(a.shape[0]):
        row_str = ""
        for j in range(a.shape[1]):
            row_str += a[i, j]
        print(row_str)

extra_count = 0
unique_paths = []
dp = np.zeros_like(arr, dtype=int)

# for row_idx in range(arr.shape[0]-1):
#     if row_idx == 0:
#         # this is the first row
#         s_idx = None
#         for j in range(arr.shape[1]):
#             if arr[row_idx, j] == 'S':
#                 s_idx = j
#                 break
#         # beneath S draw a |
#         arr[row_idx+1, s_idx] = '|'
#         unique_paths.append([(row_idx+1, s_idx)])
#     else:
#         to_append = []
#         to_pop = []
#         to_modify = []
#         for k, path in enumerate(unique_paths):
#             row, col = path[-1]
#             val = arr[row, col]
#
#             val_below = arr[row+1, col]
#             if val_below == ".":
#                 # move down
#                 # arr[row+1, col] = "|"
#                 to_modify.append([row+1, col, "|"])
#                 unique_paths[k].append((row+1, col))
#             elif val_below == "^":
#                 # split
#                 left_path = path.copy()
#                 left_path.append((row+1, col-1))
#                 right_path = path.copy()
#                 right_path.append((row+1, col+1))
#
#                 if k not in to_pop:
#                     to_pop.append(k)
#
#                 to_append.append(left_path)
#                 to_append.append(right_path)
#
#                 # if arr[row+1, col-1] == "|":
#                 #     extra_count += 1
#                 # if arr[row+1, col+1] == "|":
#                 #     extra_count += 1
#                 to_modify.append([row+1, col-1, "|"])
#                 to_modify.append([row+1, col+1, "|"])
#                 # arr[row+1, col-1] = "|"
#                 # arr[row+1, col+1] = "|"
#         unique_paths.extend(to_append)
#         for index in sorted(to_pop, reverse=True):
#             unique_paths.pop(index)
#         # modify arr
#         for mod in to_modify:
#             r, c, v = mod
#             arr[r, c] = v
#         print(len(unique_paths), "unique paths after row", row_idx)

for row_idx in range(arr.shape[0]-1):
    if row_idx == 0:
        # this is the first row
        s_idx = None
        for j in range(arr.shape[1]):
            if arr[row_idx, j] == 'S':
                s_idx = j
                break
        # beneath S draw a |
        # arr[row_idx+1, s_idx] = '|'
        dp[row_idx+1, s_idx] = 1
    else:
        for col_idx in range(arr.shape[1]):
            if dp[row_idx, col_idx] == 0:
                continue
            val = arr[row_idx, col_idx]
            if val == ".":
                dp[row_idx+1, col_idx] += dp[row_idx, col_idx]
            elif val == "^":
                dp[row_idx+1, col_idx-1] += dp[row_idx, col_idx]
                dp[row_idx+1, col_idx+1] += dp[row_idx, col_idx]
    print(dp)

print(sum(dp[-1, :]), "unique paths")
