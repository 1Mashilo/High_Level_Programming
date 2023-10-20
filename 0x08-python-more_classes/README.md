# Python - More Classes and Objects

This project explores object-oriented programming concepts in Python and includes various tasks that build upon each other to create a comprehensive understanding of class methods, static methods, special methods, class vs. instance attributes, and object-oriented design.

## Table of Contents

- [Tasks](#tasks)
  - [Task 0: Simple Rectangle](#task-0-simple-rectangle)
  - [Task 1: Real Definition of a Rectangle](#task-1-real-definition-of-a-rectangle)
  - [Task 2: Area and Perimeter](#task-2-area-and-perimeter)
  - [Task 3: String Representation](#task-3-string-representation)
  - [Task 4: Eval is Magic](#task-4-eval-is-magic)
  - [Task 5: Detect Instance Deletion](#task-5-detect-instance-deletion)
  - [Task 6: How Many Instances](#task-6-how-many-instances)
  - [Task 7: Change Representation](#task-7-change-representation)
  - [Task 8: Compare Rectangles](#task-8-compare-rectangles)
  - [Task 9: A Square is a Rectangle](#task-9-a-square-is-a-rectangle)
  - [Task 10: N Queens](#task-10-n-queens)

## Tasks

### Task 0: Simple Rectangle

[0-rectangle.py](./0-rectangle.py) defines an empty Python class that represents a rectangle.

### Task 1: Real Definition of a Rectangle

[1-rectangle.py](./1-rectangle.py) builds upon the previous task to define a Python class representing a rectangle. It includes private instance attributes for `width` and `height` with getters and setters. The class allows instantiation with optional `width` and `height` and handles data validation.

### Task 2: Area and Perimeter

[2-rectangle.py](./2-rectangle.py) extends the rectangle class to include public instance methods for calculating the area and perimeter of the rectangle. It handles cases where `width` or `height` is zero.

### Task 3: String Representation

[3-rectangle.py](./3-rectangle.py) enhances the class with a special method `__str__` to provide a string representation of the rectangle using the `#` character. If `width` or `height` is zero, the method returns an empty string.

### Task 4: Eval is Magic

[4-rectangle.py](./4-rectangle.py) introduces the `__repr__` special method to return a string representation of the rectangle, making it possible to recreate the object using `eval()`.

### Task 5: Detect Instance Deletion

[5-rectangle.py](./5-rectangle.py) adds a special method `__del__` that prints a message when a rectangle instance is deleted.

### Task 6: How Many Instances

[6-rectangle.py](./6-rectangle.py) introduces a public class attribute `number_of_instances` that tracks the number of active instances. It is incremented for each new instantiation and decremented for each instance deletion.

### Task 7: Change Representation

[7-rectangle.py](./7-rectangle.py) includes a public class attribute `class_symbol` that allows customizing the string representation of the rectangle.

### Task 8: Compare Rectangles

[8-rectangle.py](./8-rectangle.py) adds a static method `bigger_or_equal` that compares two rectangles based on their areas and returns the one with the greater area. It handles error cases when the input is not a `Rectangle` instance.

### Task 9: A Square is a Rectangle

[9-rectangle.py](./9-rectangle.py) extends the class to include a class method `square` that creates a new rectangle with equal width and height, effectively creating a square.

### Task 10: N Queens

[101-nqueens.py](./101-nqueens.py) is a Python program that solves the [N queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle). It determines all possible solutions for placing N non-attacking queens on an NxN chessboard, handling various input validation scenarios and printing solutions in a specific format.

This project provides a comprehensive exploration of object-oriented programming in Python, covering class methods, static methods, special methods, attributes, and practical applications. It also demonstrates problem-solving skills through the N queens puzzle.

