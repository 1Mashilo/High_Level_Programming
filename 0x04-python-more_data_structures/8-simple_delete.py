def delete_key_from_dictionary(dictionary, key):
    """
    Delete a key from a dictionary, if it exists.

    Args:
        dictionary (dict): The dictionary from which to delete the key.
        key (str): The key to be deleted.

    Returns:
        dict: The updated dictionary after key deletion.
    """
    if key in dictionary:
        del dictionary[key]
    return dictionary


# Test case

sample_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York',
    'country': 'USA'
}

deleted_dict = delete_key_from_dictionary(sample_dict, 'age')

print("Updated Dictionary:")
print(deleted_dict)
