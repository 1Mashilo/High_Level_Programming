

class Square:
    """A class for representing squares.

    This class allows the creation of square objects with a specified size. The size
    should be a non-negative integer. The size is stored as a private attribute, and
    validation checks ensure the size is valid during object creation.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):

        """Initialize a new Square.
        Args:
            size (int): The size of the new square. It should be a non-negative integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
