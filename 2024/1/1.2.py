from collections import Counter

def calculate_similarity_score(left_list, right_list):
    """
    Calculates the similarity score between two lists based on the number of 
    occurrences of left list items in the right list.

    Args:
      left_list: A list of integers.
      right_list: A list of integers.

    Returns:
      The total similarity score as an integer.
    """

    right_counts = Counter(right_list)
    total_score = 0
    for num in left_list:
        total_score += num * right_counts[num]
    return total_score


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

    similarity_score = calculate_similarity_score(left_numbers, right_numbers)
    print(f"The similarity score between the lists is: {similarity_score}")