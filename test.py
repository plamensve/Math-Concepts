from collections import Counter


def encode(text):
    chars = {ch: text.count(ch) for ch in dict.fromkeys(text)}

    final_string = ''
    for key, value in chars.items():
        if value == 1:
            final_string += key
        else:
            final_string += key
            final_string += str(value)

    return final_string


def decode(text):
    """
    Decodes the text using run-length encoding
    """
    code = [x for x in text]

    final_string = ''

    for char in code:
        if not char.isdigit():
            final_string += char
        else:
            final_string += code[code.index(char) - 1] * (int(code[code.index(char)]) - 1)

    return final_string


print(decode("AABCCCDEEEE"))
