#!/usr/bin/python3

def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current_index = 0
    while current_index < len(text) and text[current_index] == ' ':
        current_index += 1

    while current_index < len(text):
        print(text[current_index], end="")
        if text[current_index] == "\n" or text[current_index] in ".?:":
            if text[current_index] in ".?:":
                print("\n")
            current_index += 1
            while current_index < len(text) and text[current_index] == ' ':
                current_index += 1
            continue
        current_index += 1
