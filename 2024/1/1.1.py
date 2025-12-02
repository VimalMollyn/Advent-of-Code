def calculate_total_distance(left_list, right_list):
    """
    Calculates the total distance between two lists by pairing up the 
    sorted numbers and summing the absolute differences.

    Args:
      left_list: A list of integers.
      right_list: A list of integers.

    Returns:
      The total distance between the lists as an integer.
    """

    left_list.sort()
    right_list.sort()
    total_distance = 0
    for left_num, right_num in zip(left_list, right_list):
        total_distance += abs(left_num - right_num)
    return total_distance


if __name__ == "__main__":
    # Read input from file 
    with open("input.txt", "r") as f:
        lines = f.readlines()
    
    left_numbers = []
    right_numbers = []
    for line in lines:
        left, right = map(int, line.split())
        left_numbers.append(left)
        right_numbers.append(right)
    
    total_distance = calculate_total_distance(left_numbers, right_numbers)
    print(f"The total distance between the lists is: {total_distance}")