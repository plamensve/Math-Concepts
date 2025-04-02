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


print(encode("AABCCCDEEEE"))

# def decode(text):
#     """
#     Decodes the text using run-length encoding
#     """
#     for char in text:
#         if char.isdigit():
#             return
#
# decode("A2BC3DE4")