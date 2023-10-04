"""
Perform a custom calculation based on the values of 'a' and 'b'.

This function takes two integer values, 'a' and 'b', and performs a custom
calculation based on the values of 'a' and 'b'. It involves importing the 'add'
and 'sub' functions from the 'magic_calculation_102' module and using them to
calculate the result.

If 'a' is less than 'b', it performs a series of additions using the 'add'
function and returns the final result. Otherwise, it calculates the result using
the 'sub' function.

This function is designed to match a specific bytecode provided by Holberton School.
"""
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
