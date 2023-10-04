"""
This Python program assigns a random signed number to the variable 'number' each time it is executed
and prints its last digit along with specific conditions.

It prints the string 'Last digit of [number] is [last_digit]' followed by:
- If the number is greater than 5: 'and is greater than 5'
- If the number is 0: 'and is 0'
- If the number is less than 6 and not 0: 'and is less than 6 and not 0'
Followed by a new line.
"""

import random

number = random.randint(-10, 20)

last_digit = abs(number) % 10

if number > 5:
    message = "and is greater than 5"
elif number == 0:
    message = "and is 0"
else:
    message = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last_digit} {message}")
