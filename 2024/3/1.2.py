import re

def calculate_conditional_multiplication_sum(memory):
    """
    Scans the corrupted memory for mul, do, and don't instructions and
    sums the results of enabled multiplications.

    Args:
      memory: A string representing the corrupted memory.

    Returns:
      The sum of the results of enabled multiplication as an integer.
    """
    total_sum = 0
    enabled = True
    matches = re.finditer(r'(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))', memory)

    for match in matches:
      instruction = match.group(0)
      if instruction.startswith('mul'):
        if enabled:
            num1 = int(match.group(2))
            num2 = int(match.group(3))
            total_sum += num1 * num2
      elif instruction == "do()":
        enabled = True
      elif instruction == "don't()":
        enabled = False

    return total_sum

if __name__ == "__main__":
    # Read input from file
    with open("input.txt", "r") as f:
      memory = f.read()

    total_sum = calculate_conditional_multiplication_sum(memory)
    print(f"The sum of the enabled multiplication results is: {total_sum}")