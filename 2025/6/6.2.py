from math import prod

# Read input from file 
with open("input.txt", "r") as f:
    lines = f.readlines()
    # lines = [x.strip("\n") for x in lines]


# go column by column
operators = [x.strip() for x in lines[-1].strip().split(' ') if x != ""]
all_problems = []
problem = []
for i_col in range(len(lines[0])):
    col_str = ""
    for j_row in range(len(lines)-1):
        char = lines[j_row][i_col]
        col_str += char
    if col_str == " "*(len(lines)-1) or "\n" in col_str:
        # now it's a new problem
        all_problems.append(problem)
        problem = []
    else:
        problem.append(int(col_str))

print(all_problems)


total = 0
for o, problem in zip(operators, all_problems):
    if o == '+':
        result = sum(problem)
        print("+".join(str(x) for x in problem), "=", result)
    elif o == '*':
        result = prod(problem)
        print("*".join(str(x) for x in problem), "=", result)
    total += result
print(total)



