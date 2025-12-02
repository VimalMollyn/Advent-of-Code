import re

def calculate_multiplication_sum(memory):
    """
    Scans the corrupted memory for valid mul instructions and sums the results.

    Args:
      memory: A string representing the corrupted memory.

    Returns:
      The sum of the multiplication results as an integer.
    """
    total_sum = 0
    matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', memory)
    for match in matches:
        num1, num2 = int(match[0]), int(match[1])
        total_sum += num1 * num2
    return total_sum

if __name__ == "__main__":
    # Read input from file
    with open("input.txt", "r") as f:
        memory = f.read()

    total_sum = calculate_multiplication_sum(memory)
    print(f"The sum of the multiplication results is: {total_sum}")