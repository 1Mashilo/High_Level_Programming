def print_sorted_dictionary(a_dictionary):

    """
    Print the keys and values of a dictionary in sorted order.

    Args:
        a_dictionary (dict): The dictionary to be sorted and printed.

    Returns:
        None
    """

    sorted_keys = list(a_dictionary.keys())
    sorted_keys.sort()

    for key in sorted_keys:
        value = a_dictionary.get(key)
        print("{}: {}".format(key, value))

# Define a sample dictionary
sample_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'country': 'USA'
}

# Call the function to print the dictionary in sorted order
print("Sorted Dictionary:")
print_sorted_dictionary(sample_dict)
