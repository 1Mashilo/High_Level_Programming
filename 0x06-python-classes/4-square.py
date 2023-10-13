

class Square:
    """
    A class representing a square.

    This class allows you to create square objects with a specified size, 
    and it enforces that the size is a non-negative integer.

    Attributes:
        size (int): The size of the square.

    Methods:
        area(): Calculate and return the area of the square.

    """

    def __init__(self, size=0):
        """
        Initialize a new square with a given size.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """
        Get or set the current size of the square.

        The size of the square must be a non-negative integer.

        Returns:
            int: The size of the square.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is a negative integer.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (size^2).
        """
        return self.__size * self.__size
