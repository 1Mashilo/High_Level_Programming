def fizz_buzz():
    """
    Print numbers from 1 to 100 with Fizz for multiples of 3, Buzz for multiples of 5,
    and FizzBuzz for multiples of both 3 and 5.

    This function iterates through numbers from 1 to 100 and applies the FizzBuzz rules:
    - For multiples of 3, "Fizz" is printed.
    - For multiples of 5, "Buzz" is printed.
    - For multiples of both 3 and 5, "FizzBuzz" is printed.
    - For all other numbers, the number itself is printed.

    No additional modules are imported.

    Returns:
        None
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")

# Call the function to print the FizzBuzz sequence
fizz_buzz()
