def update_dictionary(dictionary, key, value):
    """
    Replace or add a key/value pair in a dictionary.

    Args:
        dictionary (dict): The dictionary to be updated.
        key (str): The key to be added or updated.
        value: The value to be associated with the key.

    Returns:
        dict: The updated dictionary.
    """
    dictionary[key] = value
    return dictionary

# Test case
if __name__ == "__main__":
    # Create an initial dictionary
    my_dict = {'name': 'Alice', 'age': 25}

    # Print the initial dictionary
    print("Initial Dictionary:", my_dict)

    # Update the dictionary with a new key-value pair
    updated_dict = update_dictionary(my_dict, 'city', 'New York')

    # Print the updated dictionary
    print("Updated Dictionary:", updated_dict)
