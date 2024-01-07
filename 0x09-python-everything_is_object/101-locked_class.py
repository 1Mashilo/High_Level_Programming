#!/usr/bin/python3
class LockedClass:
    """
    This class defines a LockedClass that allows only the 'first_name' attribute to be set.

    Attributes:
        first_name (str): The first name of the instance.
    """
    __slots__ = ('first_name',)
