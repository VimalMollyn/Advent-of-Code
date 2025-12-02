# Read input from file 
with open("input.txt", "r") as f:
    lines = f.readlines()[0].strip().split(",")

total = 0
for line in lines:
    if "-" not in line:
        continue
    a, b = line.split("-")

    a = int(a)
    b = int(b)
    for i in range(a, b + 1):
        # if odd skip
        i_str = str(i)
        if len(i_str) % 2 != 0:
            continue
        half_len = len(i_str) // 2
        if i_str[:half_len] == i_str[half_len:]:
            print(i)
            total += i
print("Total:", total)


