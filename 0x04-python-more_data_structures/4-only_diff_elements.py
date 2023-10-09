def only_diff_elements(set1, set2):
    """
    Find the elements that are unique to each set and not common to both sets.

    Args:
        set1 (set): The first set.
        set2 (set): The second set.

    Returns:
        set: A set containing the elements that are unique to each set (symmetric difference).
    """
    return set1 ^ set2
