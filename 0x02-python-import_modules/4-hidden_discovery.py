#!/usr/bin/python3
if __name__ == "__main__":
    """List Public Names in hidden_4 Module

    This script imports the hidden_4 module and lists all the publicly
    accessible names defined within it. Names starting with double
    underscores (__) are considered hidden and are excluded from the list.

    """
    import hidden_4
    for name in dir(hidden_4):
        if name[0] != '_' and name[1] != '_':
            print(name)
            