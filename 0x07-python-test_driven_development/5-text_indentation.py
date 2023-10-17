
def text_indentation(text):
    """
    Split a text into lines along '?', ':', or '.', followed by two new lines.

    Args:
        text (str): The text to be split into lines.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    newline_flag = True
    for character in text:
        if newline_flag:
            if character == ' ':
                continue
            else:
                newline_flag = False
        if not newline_flag:
            if character in ['?', '.', ':']:
                print(character)
                print()
                newline_flag = True
            else:
                print(character, end="")
