#!/usr/bin/python3

def raise_exception_msg(message=""):
    """
    Raise a NameError exception with an optional custom message.

    This function raises a built-in Python exception called `NameError` and allows an optional custom message to be
    included when raising the exception. The custom message, if provided, should be a string.

    Args:
        message (str, optional): An optional custom message to include in the exception.

    Raises:
        NameError: This exception is raised with the provided custom message or an empty string if no message is
        provided.
    """
    raise NameError(message)
