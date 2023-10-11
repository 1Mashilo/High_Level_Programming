
def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x integer elements from a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The maximum number of integer elements from my_list to print.

    Returns:
        int: The count of integer elements successfully printed.
    """
    elements_printed_count = 0 
    for index in range(0, x):  
        try:
            element = my_list[index]
            if isinstance(element, int): 
                print(f"{element:d}", end="")  
                elements_printed_count += 1 
        except (ValueError, TypeError):
            continue  
    print("")  
    return elements_printed_count 