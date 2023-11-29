#!/usr/bin/python3
"""
Prints numbers from 0 to 99 with two digits each.

This program uses a loop to iterate through numbers from 0 to 99,
and it ensures that each number is displayed
with two digits. Numbers are separated by a comma and space except
for the last number, which is followed by a new line.

"""
for num in range(0, 99):
    print('{:02d}, '.format(num), end='')
print('99')