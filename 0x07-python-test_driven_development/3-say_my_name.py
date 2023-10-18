def say_my_name(first_name, last_name=""):
    """
    Return a message in the format: "My name is <first_name> <last_name>."

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string, or last_name is an empty string.
    """
    if not isinstance(first_name, str) or (not isinstance(last_name, str) or last_name == ""):
        raise TypeError("Both first_name and last_name must be non-empty strings")
    return f"My name is {first_name} {last_name}"
