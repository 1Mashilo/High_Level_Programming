#!/usr/bin/python3

def safe_print_list(my_list, x):
    
    """Print x elements of a list, handling exceptions gracefully.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to print.

    Returns:
        int: The number of elements successfully printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end=" ")
            ret += 1
        except IndexError:
            break
    print("") 
    return ret

