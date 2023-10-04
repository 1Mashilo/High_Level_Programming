if __name__ == "__main__":
    """
    Print information about the command-line arguments.

    This script calculates and displays the number of command-line arguments
    provided when running the script, along with a list of the arguments and
    their positions.
    """
    import sys

    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("No arguments provided.")
    elif num_args == 1:
        print("One argument provided:")
    else:
        print(f"{num_args} arguments provided:")

    for i in range(num_args):
        print(f"Argument {i + 1}: {sys.argv[i + 1]}")

