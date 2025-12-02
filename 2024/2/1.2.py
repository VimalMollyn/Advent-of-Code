def is_safe_report(levels):
    """
    Checks if a report is safe according to the specified rules.

    Args:
      levels: A list of integers representing the levels in a report.

    Returns:
      True if the report is safe, False otherwise.
    """
    if len(levels) <= 1:
        return True  # A single level or empty report is considered safe

    increasing = None  # None, True, or False

    for i in range(len(levels) - 1):
        diff = levels[i+1] - levels[i]

        if abs(diff) < 1 or abs(diff) > 3:
            return False  # Difference not within allowed range

        if increasing is None:
            increasing = diff > 0 # Set based on the first diff

        elif (diff > 0 and not increasing) or (diff < 0 and increasing):
            return False  # Inconsistent direction

    return True

def is_safe_with_dampener(levels):
    """
    Checks if a report is safe, including checking for a single removable level
    that would make it safe.

    Args:
        levels: A list of integers representing the levels in a report.

    Returns:
      True if the report is safe with or without removing a single level,
      False otherwise.
    """

    if is_safe_report(levels):
       return True

    for i in range(len(levels)):
       temp_levels = levels[:i] + levels[i+1:] # remove level at position i
       if is_safe_report(temp_levels):
           return True
    
    return False


if __name__ == "__main__":
    # Read input from file
    with open("input.txt", "r") as f:
        lines = f.readlines()

    safe_report_count = 0
    for line in lines:
        levels = list(map(int, line.split()))
        if is_safe_with_dampener(levels):
            safe_report_count += 1

    print(f"The number of safe reports with dampener is: {safe_report_count}")