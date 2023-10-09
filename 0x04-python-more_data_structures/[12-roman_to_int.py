def roman_to_integer(roman_string):
    """
    Convert a Roman numeral to an integer.

    Args:
        roman_string (str): The Roman numeral to be converted.

    Returns:
        int: The integer equivalent of the Roman numeral.
             Returns 0 if the input is not a valid Roman numeral.
    """
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    prev_value = 0

    for char in roman_string[::-1]:
        value = roman_dict.get(char, 0)

        if value < prev_value:
            result -= value
        else:
            result += value

        prev_value = value

    return result

# Test case
if __name__ == "__main__":
    roman_numeral = "IX"
    converted_integer = roman_to_integer(roman_numeral)
    print(f"The Roman numeral {roman_numeral} is equivalent to {converted_integer}.")
