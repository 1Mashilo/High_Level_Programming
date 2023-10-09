def multiply_list_map(my_list=[], number=0):
    """
    Multiply each element in the input list by a specified number using `map`.

    Args:
        my_list (list, optional): The input list of numbers. Defaults to an empty list.
        number (int, optional): The number by which each element in the list will be multiplied. Defaults to 0.

    Returns:
        list: A new list with each value from `my_list` multiplied by `number`.
    """
    return list(map((lambda i: i * number), my_list))

# Test case
if __name__ == "__main__":
    input_list = [1, 2, 3, 4]
    multiplier = 5
    result = multiply_list_map(input_list, multiplier)
    print("Original List:", input_list)
    print("Multiplier:", multiplier)
    print("Result:", result)
