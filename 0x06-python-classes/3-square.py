#!/usr/bin/python3

class Square:
    """A class that represents a square.

    This class allows the creation of square objects with a specified size,
    and it enforces that the size is a non-negative integer. Additionally, it
    provides a method to calculate the area of the square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        area(): Calculate and return the area of the square.
    """

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square. It must be a non-negative integer.
        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is a negative integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        
        """Calculate and return the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return (self.__size * self.__size)
