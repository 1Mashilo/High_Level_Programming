
class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle object with optional width and height.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is less than 0.
        """
        self.__width = width 
        self.__height = height  

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        
        """
        Calculate and return the perimeter of the rectangle.
        
        The perimeter is 0 if either the width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return  ((self.__width * 2) + (self.__height * 2))
    
    def __str__(self):
        """
        Return a string representation of the rectangle using the '#' character.

        If either the width or height is 0, an empty string is returned.
       """
        if self.__width == 0 or self.__height == 0:
           return ""
           
        rectangle_str = "" 
        for _ in range(self.__height):
           rectangle_str += "#" * self.__width + "\n" 
        return rectangle_str.rstrip() 
    
    def __repr__(self):

      """Return the string representation of the Rectangle."""
   
      representation = "Rectangle("

      representation += str(self.__width)
      representation += ", "  
      representation += str(self.__height)

      representation += ")"
      return representation

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2
    
    @classmethod
    def square(cls, size=0):
        return cls(size, size)