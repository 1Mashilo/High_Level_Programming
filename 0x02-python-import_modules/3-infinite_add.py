if __name__ == "__main__":
    """
    Calculate and print the sum of command-line arguments.

    This script calculates the sum of all command-line arguments provided when
    running the script and prints the result.
    """
    import sys

    total = 0

    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])

    print(f"Sum of provided arguments: {total}")
