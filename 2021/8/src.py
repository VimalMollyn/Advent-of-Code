input_file = 'input.txt'

# parse the input file
with open(input_file, 'r') as f:
    lines = f.readlines()

# for each line, get the input and the output
# the input and output are separated by a " | "
count = 0
for line in lines:
    input_output = line.strip().split(' | ')
    input = input_output[0].split(" ")
    output = input_output[1].split(" ")
    # print(input, output)

    # for each output, check if the number of characters is in [2, 4, 3, 7]
    # if so, increment the count
    for o in output:
        if len(o) in [2, 4, 3, 7]:
            # print(o)
            count += 1

print(count)

# part 2

# loop through the lines
numbers = []
for line in lines:
    a=b=c=d=e=f=g=None
    input_output = line.strip().split(' | ')
    input = input_output[0].split(" ")
    output = input_output[1].split(" ")

    # store each input in a dictionary, based on the length of the input_file
    # the key is the length of the input, and the value is a list of inputs
    # with that length
    input_dict = {}
    for i in input:
        if len(i) in input_dict:
            input_dict[len(i)].append(i)
        else:
            input_dict[len(i)] = [i]

    a = set(input_dict[3][0]) - set(input_dict[2][0]) # 7 - 1
    e_g = set('abcdefg') - set(input_dict[3][0]).union(set(input_dict[2][0]), set(input_dict[4][0])) # 8 - (7+4)
    a_b_f_g = set(input_dict[6][0]).intersection(set(input_dict[6][1]), input_dict[6][2]) # 6U9 - 6I9
    e = e_g - a_b_f_g 
    g = e_g - e
    b_f = a_b_f_g - g - a
    b_d = set(input_dict[4][0]) - set(input_dict[2][0])
    b = b_f.intersection(b_d)
    d = b_d - b
    f = b_f - b
    c = set('abcdefg') - a - b - d - e - f - g

    letters2numbers = {
            'abcefg': 0,
            'cf': 1,
            'acdeg': 2,
            'acdfg': 3,
            'bcdf': 4,
            'abdfg': 5,
            'abdefg': 6,
            'acf': 7,
            'abcdefg': 8,
            'abcdfg': 9
            }

    code = {
            list(a)[0]: 'a',
            list(b)[0]: 'b',
            list(c)[0]: 'c',
            list(d)[0]: 'd',
            list(e)[0]: 'e',
            list(f)[0]: 'f',
            list(g)[0]: 'g'
            }

    # for each word in output, decode it and convert to a number
    decoded_output = []
    for output_word in output:
        decoded_word = []
        for letter in output_word:
            decoded_word.append(code[letter])

        # convert the decoded word to a letters2number number
        decoded_number = letters2numbers["".join(sorted(decoded_word))]
        decoded_output.append(decoded_number)

    number = int("".join([str(x) for x in decoded_output]))
    print(" ".join(output), number)
    numbers.append(number)

print(f"Answer: {sum(numbers)}")
