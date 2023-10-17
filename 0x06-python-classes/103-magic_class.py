

import math

class MagicClass:
    """
    Represent a circle and provide methods for area and circumference calculations.

    Attributes:
        __radius (float or int): The radius of the circle.

    Args:
        radius (float or int): The radius of the new circle.
    """

    def __init__(self, radius=0):
        """
        Initialize a MagicClass with a given radius.

        Args:
            radius (float or int): The radius of the new circle. It must be a number.
        
        Raises:
            TypeError: If the provided radius is not a number (int or float).
        """
        self.__radius = 0  

        
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.

        Returns:
            float: The area of the circle, calculated as pi times the radius squared.
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Calculate and return the circumference of the circle.

        Returns:
            float: The circumference of the circle, calculated as 2 times pi times the radius.
        """
        return (2 * math.pi * self.__radius)
