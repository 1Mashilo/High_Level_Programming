"""
This Python script concatenates two strings and prints a welcome message.

It assigns the strings "Holberton" and "School" to 'str1' and 'str2', respectively. 
Then, it concatenates 'str1' and 'str2' with a space in between and prints a welcome message using string formatting.
"""

str1 = "Holberton"
str2 = "School"

str1 += " " + str2
print("Welcome to {}!".format(str1))
