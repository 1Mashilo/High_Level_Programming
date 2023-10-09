def weight_average(my_list=[]):
    """
    Calculate the weighted average of a list of tuples.

    Args:
        my_list (list, optional): The list of tuples, where each tuple contains a numeric value and its weight.
                                  Defaults to an empty list.

    Returns:
        float: The weighted average of the values in the list of tuples.
               Returns 0 if the input list is empty.
    """
    if not my_list:
        return 0

    num = 0 
    den = 0  

    for tup in my_list:
        num += tup[0] * tup[1] 
        den += tup[1]          

    return (num / den) 
