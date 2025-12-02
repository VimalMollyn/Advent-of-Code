# Read input from file 
with open("input.txt", "r") as f:
    lines = f.readlines()

curr_pos = 50
ans = 0
for line in lines:
    command = line[0]
    value = int(line[1:])
    if command == "L":
        for _i in range(value):
            curr_pos -= 1
            curr_pos = curr_pos%100
            if curr_pos == 0:
                ans += 1
    elif command == "R":
        for _i in range(value):
            curr_pos += 1
            curr_pos = curr_pos%100
            if curr_pos == 0:
                ans += 1

    # print(curr_pos)
    # curr_pos = curr_pos % 100
    #
    # if curr_pos == 0:
    #     ans += 1
print(ans)

