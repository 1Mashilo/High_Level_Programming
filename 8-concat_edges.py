"""
This Python script demonstrates string manipulation.

It extracts specific portions from a long string and concatenates them to create a new string.
"""

# Define a long string describing Python's characteristics
original_str = "Python is an interpreted, interactive, object-oriented programming" \
               " language that combines remarkable power with very clear syntax"

# Extract three portions from the original string and concatenate them
# - Characters 40 to 66 (inclusive)
# - Characters 108 to 111 (inclusive)
# - First 6 characters
new_str = original_str[39:67] + original_str[107:112] + original_str[:6]

# Print the resulting string
print(new_str)
