def multiply_values_by_2(input_dict):

    """
    Create a new dictionary with values doubled from the input dictionary.

    Args:
        input_dict (dict): The dictionary from which values will be doubled.

    Returns:
        dict: A new dictionary with the same keys and values doubled.
    """
    # Create a copy of the input dictionary
    doubled_dict = input_dict.copy()

    # Get a list of keys from the copied dictionary
    keys_list = list(doubled_dict.keys())

    # Iterate through keys and double values
    for key in keys_list:
        doubled_dict[key] *= 2

    return doubled_dict

# Test case 

# Define a sample dictionary with integer values
sample_dict = {
    'a': 5,
    'b': 10,
    'c': 15,
    'd': 20
}

# Call the function to create a new dictionary with doubled values
doubled_dict = multiply_values_by_2(sample_dict)

# Print the original and modified dictionaries
print("Original Dictionary:")
print(sample_dict)

print("\nModified Dictionary:")
print(doubled_dict)
