#!/usr/bin/python3

if __name__ == "__main__":
    """
    Handle basic arithmetic operations.

    Usage: ./100-my_calculator.py <a> <operator> <b>

    This script performs basic arithmetic operations based on user input. It supports
    addition (+), subtraction (-), multiplication (*), and division (/).

    Args:
        <a>: The first operand (an integer).
        <operator>: The arithmetic operator (+, -, *, or /).
        <b>: The second operand (an integer).

    Example usage:
        $ ./100-my_calculator.py 5 + 3
        5 + 3 = 8

    If the input is not provided correctly or an unknown operator is used, the script
    provides appropriate error messages and exits with a status code of 1.
    """
    from calculator_1 import add, sub, mul, div 
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(ops.keys()):
        print(f"Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print(f"{a} {sys.argv[2]} {b} = {ops[sys.argv[2]](a, b)}")
