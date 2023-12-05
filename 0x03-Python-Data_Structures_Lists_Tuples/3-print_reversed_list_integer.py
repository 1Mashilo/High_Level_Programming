
#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Print all integers of a list in reverse order.

    Args:
        my_list (list of int): The list of integers to be printed in reverse order.
    """
    
    if not isinstance(my_list, list):
        print("Input is not a list.")
        return

    reversed_list = my_list[::-1]
    
    for i in reversed_list:
        print("{:d}".format(i))
