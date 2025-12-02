# Read input from file 
with open("input.txt", "r") as f:
    lines = f.readlines()

curr_pos = 50
ans = 0
for line in lines:
    command = line[0]
    value = int(line[1:])
    if command == "L":
        curr_pos -= value
    elif command == "R":
        curr_pos += value

    curr_pos = curr_pos%100
    # print(curr_pos)

    if curr_pos == 0:
        ans += 1
print(ans)

