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
        l_i_str = len(i_str)

        # find all divisors of len(i_str)
        divisors = []
        for d in range(1, int(l_i_str**0.5) + 1):
            if l_i_str % d == 0:
                divisors.append(d)
                other_d = l_i_str // d
                if other_d != d:
                    divisors.append(other_d)

        # remove all divisors greater than half len
        divisors = [d for d in divisors if d <= l_i_str // 2]

        for d in divisors:
            # print("the divisor:", d, divisors)
            if l_i_str % d != 0:
                continue

            part_len = d
            first_part = i_str[:part_len]

            all_parts_equal = True
            for n in range(1, l_i_str // part_len):
                part = i_str[n * part_len : (n + 1) * part_len]
                all_parts_equal = all_parts_equal and (part == first_part)
                if all_parts_equal == False:
                    break
            if all_parts_equal:
                total += i
                print("Adding:", i)
                break

            

print("Total:", total)


