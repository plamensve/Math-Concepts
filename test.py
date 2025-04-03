import re


def encode(text):
    """
    Returns the run-length encoded version of the text
    (numbers after symbols, length = 1 is skipped)
    """
    my_list = []
    current_string = ''
    for i in range(len(text)):

        if text[i] == current_string[:1] or current_string == '':
            current_string += text[i]
        else:
            my_list.append(f"{current_string[:1]}{len(current_string)}")
            current_string = ''
            current_string += text[i]

    my_list.append(f"{current_string[:1]}{len(current_string)}")

    result = "".join(my_list)
    result = result.replace('1', '')
    return result


def decode(text):
    pattern = re.findall(r'([A-Z])(\d*)', text)

    result = ''
    for char, count in pattern:
        num = int(count) if count else 1
        result += char * num

    return result


print(encode('A3TGC3TA2CTAGAT2GA3C3G2T'))
