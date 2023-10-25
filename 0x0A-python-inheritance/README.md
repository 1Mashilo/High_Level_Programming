# Python Inheritance Project

In this project, we explore the concept of class inheritance in Python. Inheritance allows us to create new classes that are built upon existing classes, inheriting their attributes and methods. We delve into the differences between super- and sub-classes, practice defining classes with multiple base classes, and learn about overriding inherited methods and attributes.

## Tests :heavy_check_mark:

- [Tests Folder](./tests): This directory contains various test files.

## Function Prototypes :floppy_disk:

Here are the function prototypes defined in this project:

| File                    | Prototype                             |
| ----------------------- | ------------------------------------- |
| `0-lookup.py`           | `def lookup(obj):`                    |
| `1-my_list.py`          | `class MyList(list)`                 |
|                         | `def print_sorted(self):`             |
| `2-is_same_class.py`    | `def is_same_class(obj, a_class):`    |
| `3-is_kind_of_class.py` | `def is_kind_of_class(obj, a_class):` |
| `4-inherits_from.py`    | `def inherits_from(obj, a_class):`    |
| `5-base_geometry.py`    | `class BaseGeometry:`                 |
| `6-base_geometry.py`    | `class BaseGeometry:`                 |
|                         | `def area(self):`                     |
| `7-base_geometry.py`    | `class BaseGeometry:`                 |
|                         | `def integer_validator(self, name, value):` |
| `8-rectangle.py`        | `class Rectangle(BaseGeometry):`      |
|                         | `def __init__(self, width, height):`   |
| `9-rectangle.py`        | `class Rectangle(BaseGeometry):`      |
|                         | `def area(self):`                     |
|                         | `def __str__(self):`                  |
| `10-square.py`          | `class Square(Rectangle):`            |
|                         | `def __init__(self, size):`           |
|                         | `def area(self):`                     |
| `11-square.py`          | `class Square(Rectangle):`            |
|                         | `def __str__(self):`                  |
| `100-my_int.py`         | `class MyInt(int):`                  |
| `101-add_attribute.py`  | `def add_attribute(obj, att, value):` |

## Project Tasks :page_with_curl:

### 0. Lookup
- [0-lookup.py](./0-lookup.py): Defines a Python function that returns a list of available attributes and methods of an object.

### 1. My List
- [1-my_list.py](./1-my_list.py): Introduces a Python class `MyList` that inherits from `list`. It includes a public instance method, `print_sorted(self)`, which prints the list in ascending sorted order. This assumes that all list elements are integers.

### 2. Exact Same Object
- [2-is_same_class.py](./2-is_same_class.py): A Python function that returns `True` if an object is exactly an instance of a specified class, and `False` otherwise.

### 3. Same Class or Inherit From
- [3-is_kind_of_class.py](./3-is_kind_of_class.py): A Python function that returns `True` if an object is an instance or an inherited instance of a specified class, and `False` otherwise.

### 4. Only Subclass Of
- [4-inherits_from.py](./4-inherits_from.py): A Python function that returns `True` if an object is an inherited instance, either directly or indirectly, from a specified class, and `False` otherwise.

### 5. Geometry Module
- [5-base_geometry.py](./5-base_geometry.py): Introduces an empty Python class, `BaseGeometry`.

### 6. Improve Geometry
- [6-base_geometry.py](./6-base_geometry.py): Enhances the `BaseGeometry` class with a public instance method, `area(self)`, which raises an `Exception` with the message "area() is not implemented."

### 7. Integer Validator
- [7-base_geometry.py](./7-base_geometry.py): Further develops the `BaseGeometry` class by adding a public instance method, `integer_validator(self, name, value)`, which validates the parameter `value`. It assumes that the parameter `name` is always a string and raises a `TypeError` exception if the value is not an integer or if it is not greater than 0.

### 8. Rectangle
- [8-rectangle.py](./8-rectangle.py): Defines a Python class, `Rectangle`, which inherits from `BaseGeometry`. This class includes private attributes, `width` and `height`, which are validated with the `integer_validator`. It also allows instantiation with `width` and `height`.

### 9. Full Rectangle
- [9-rectangle.py](./9-rectangle.py): Enhances the `Rectangle` class with an implementation of the `area()` method. It also adds a special method, `__str__`, to print rectangles in the format "[Rectangle] <width>/<height>".

### 10. Square #1
- [10-square.py](./10-square.py): Introduces the Python class `Square`, which inherits from `Rectangle`. This class includes a private attribute, `size`, which is validated with the `integer_validator`. It allows instantiation with `size` and implements the `area()` method.

### 11. Square #2
- [11-square.py](./11-square.py): Builds upon the `Square` class from Task 10 by adding a special method, `__str__`, to print squares in the format "[Square] <width>/<height>".

### 12. My Integer
- [100-my_int.py](./100-my_int.py): Defines the Python class `MyInt`, which inherits from `int`. It includes the inversion of the `==` and `!=` operators.

### 13. Can I?
- [101-add_attribute.py](./101-add_attribute.py): Provides a Python function that adds a new attribute to an object if possible. If an attribute cannot be added, it raises a `TypeError` exception with the message "can't add a new attribute."
