def search_replace(my_list, search, replace):
    """
    Replace all occurrences of an element in a list with another element and return a new list.

    Args:
        my_list (list): The initial list.
        search: The element to replace in the list.
        replace: The new element to replace 'search' with.

    Returns:
        list: A new list with all occurrences of 'search' replaced by 'replace'. The original list is not modified.
    """

    new_list = list(map(lambda x: replace if x == search else x, my_list))
    
    return new_list

