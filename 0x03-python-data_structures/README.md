# Python - Data Structures: Lists, Tuples

This project explores the fundamentals of sequence data types in Python, specifically focusing on lists and tuples.

## Table of Contents

- [Tests](#tests)
- [Function Prototypes](#function-prototypes)
- [Tasks](#tasks)

## Tests :heavy_check_mark:

- [tests](./tests): This directory contains test files provided by ALX School.

## Function Prototypes :floppy_disk:

Below are the function prototypes for each task in this project:

| File                               | Prototype                                      |
| ---------------------------------- | ---------------------------------------------- |
| `0-print_list_integer.py`          | `def print_list_integer(my_list=[]):`          |
| `1-element_at.py`                  | `def element_at(my_list, idx):`                |
| `2-replace_in_list.py`             | `def replace_in_list(my_list, idx, element):`  |
| `3-print_reversed_list_integer.py` | `def print_reversed_list_integer(my_list=[]):` |
| `4-new_in_list.py`                 | `def new_in_list(my_list, idx, element):`      |
| `5-no_c.py`                        | `def no_c(my_string):`                         |
| `6-print_matrix_integer.py`        | `def print_matrix_integer(matrix=[[]]):`       |
| `7-add_tuple.py`                   | `def add_tuple(tuple_a=(), tuple_b=()):`       |
| `8-multiple_returns.py`            | `def multiple_returns(sentence):`              |
| `9-max_integer.py`                 | `def max_integer(my_list=[]):`                 |
| `10-divisible_by_2.py`             | `def divisible_by_2(my_list=[]):`              |
| `11-delete_at.py`                  | `def delete_at(my_list=[], idx=0):`            |
| `100-print_python_list_info.c`     | `void print_python_list_info(PyObject *p);`    |

## Tasks :page_with_curl:

Here are the tasks covered in this project:

### 0. Print a list of integers
- File: [0-print_list_integer.py](./0-print_list_integer.py)
- Description: Python function that prints all integers of a list, one per line.
- Constraints: Without importing modules or casting integers into strings.

### 1. Secure access to an element in a list
- File: [1-element_at.py](./1-element_at.py)
- Description: Python function that retrieves an element from a list.
- Constraints: If `idx` is negative or out of range, the function returns `None`. Without importing modules or using `try/except`.

### 2. Replace element
- File: [2-replace_in_list.py](./2-replace_in_list.py)
- Description: Python function that replaces an element of a list at a specific position.
- Constraints: If `idx` is negative or out of range, the function returns the original list. Without importing modules or using `try/except`.

### 3. Print a list of integers... in reverse!
- File: [3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py)
- Description: Python function that prints all integers of a list, one per line, in reverse order.
- Constraints: Without importing modules or casting integers into strings.

### 4. Replace in a copy
- File: [4-new_in_list.py](./4-new_in_list.py)
- Description: Python function that replaces an element of a list at a specific position without modifying the original list.
- Constraints: If `idx` is negative or out of range, the function returns the original list. Without importing modules or using `try/except`.

### 5. Can you C me now?
- File: [5-no_c.py](./5-no_c.py)
- Description: Python function that removes all characters `c` and `C` from a string and returns the string.
- Constraints: Without importing modules or using `str.replace()`.

### 6. Lists of lists = Matrix
- File: [6-print_matrix_integer.py](./6-print_matrix_integer.py)
- Description: Python function that prints a matrix of integers, one row per line.
- Constraints: Without casting integers into strings.

### 7. Tuples addition
- File: [7-add_tuple.py](./7-add_tuple.py)
- Description: Python function that adds two tuples and returns a tuple with the sum of elements.
- Constraints: If a tuple has fewer than 2 elements, the value `0` is used for the missing integer. If a tuple has more than 2 elements, only the first two integers are used. Without importing modules.

### 8. More returns!
- File: [8-multiple_returns.py](./8-multiple_returns.py)
- Description: Python function that returns a tuple with the length of a string and its first character.
- Constraints: If the string is empty, the first character should equal `None`. Without importing modules.

### 9. Find the max
- File: [9-max_integer.py](./9-max_integer.py)
- Description: Python function that finds the biggest integer of a list.
- Constraints: If the list is empty, the function returns `None`. Without importing modules or using the builtin `max()`.

### 10. Only by 2
- File: [10-divisible_by_2.py](./10-divisible_by_2.py)
- Description: Python function that finds all multiples of 2 in a list and returns a new list of the same size.
- Constraints: Each element of the new list contains either `True` or `False` corresponding to whether the integer at the same position in the original list is a multiple of 2. Without importing modules.

### 11. Delete at
- File: [11-delete_at.py](./11-delete_at.py)
- Description: Python function that deletes an item at a specific position in a list.
- Constraints: If `idx` is negative or out of range, the function returns the original list. Without importing modules or using `pop()`.

### 12. Switch
- File: [12-switch.py](./12-switch.py)
- Description: Python program that switches the values of variable `a` and `b`.
- Completion of [this source code](https://github.com/holbertonschool/0x03.py/blob/master/12-switch_py).

### 13. Linked list palindrome
- File: [13-is_palindrome.c](./13-is_palindrome.c)
- Description: C function that checks if a singly-linked list is a palindrome.
- Constraints: If the list is a palindrome, it returns `1`. If not, it returns `0`. An empty list is considered a palindrome. Helper files: [linked_lists.c](./linked_lists.c) and [lists.h](./lists.h).

### 14. CPython #0: Python lists
- File: [100-print_python_list_info.c](./100-print_python_list_info.c)
- Description: C function that prints basic information about Python lists.

