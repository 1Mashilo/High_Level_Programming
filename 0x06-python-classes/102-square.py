

class Square:
    """Represent a square and provide comparison methods."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square and enforce data validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is a negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """Define the == comparison between two squares based on their areas.

        Args:
            other (Square): The other square to compare to.

        Returns:
            bool: True if the areas of both squares are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison between two squares based on their areas.

        Args:
            other (Square): The other square to compare to.

        Returns:
            bool: True if the areas of both squares are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison between two squares based on their areas.

        Args:
            other (Square): The other square to compare to.

        Returns:
            bool: True if the area of this square is less than the other, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison between two squares based on their areas.

        Args:
            other (Square): The other square to compare to.

        Returns:
            bool: True if the area of this square is less than or equal to the other, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison between two squares based on their areas.

        Args:
            other (Square): The other square to compare to.

        Returns:
            bool: True if the area of this square is greater than the other, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison between two squares based on their areas.

        Args:
            other (Square): The other square to compare to.

        Returns:
            bool: True if the area of this square is greater than or equal to the other, False otherwise.
        """
        return self.area() >= other.area()


