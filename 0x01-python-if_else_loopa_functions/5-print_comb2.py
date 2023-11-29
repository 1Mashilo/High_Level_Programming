#!/usr/bin/python3
"""
Prints numbers from 0 to 99 with two digits each.

This program uses a loop to iterate through numbers from 0 to 99,
and it ensures that each number is displayed
with two digits. Numbers are separated by a comma and space except
for the last number, which is followed by a new line.

"""

for number in range(100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
