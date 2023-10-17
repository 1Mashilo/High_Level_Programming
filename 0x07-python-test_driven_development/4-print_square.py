

def print_square(square_size):
    """
    Print a square using '#' characters.

    Args:
        square_size (int): The size (side length) of the square.

    Raises:
        TypeError: If square_size is not an integer.
        ValueError: If square_size is less than 0.
    """
    if type(square_size) is not int:
        raise TypeError("square_size must be an integer")
    if square_size < 0:
        raise ValueError("square_size must be >= 0")
    if square_size > 0:
        print(("#" * square_size + "\n") * square_size, end="")
