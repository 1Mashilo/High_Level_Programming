#!/usr/bin/python3
if __name__ == "__main__":
    """List Public Names in hidden_4 Module

    This script imports the hidden_4 module and lists all the publicly
    accessible names defined within it. Names starting with double
    underscores (__) are considered hidden and are excluded from the list.

    """
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
