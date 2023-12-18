#!/usr/bin/python3

def list_division(list1, list2, length):
    """
    Divide two lists element by element.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.
        length (int): The number of elements to divide.

    Returns:
        list: A new list of length `length` containing all the divisions.
    """
    result = []
    for i in range(length):
        try:
            quotient = list1[i] / list2[i]
        except TypeError:
            print("Wrong type: Skipping element")
            quotient = 0
        except ZeroDivisionError:
            print("Division by 0: Setting result to 0")
            quotient = 0
        except IndexError:
            print("Out of range: Setting result to 0")
            quotient = 0
        finally:
            result.append(quotient)

    return result
