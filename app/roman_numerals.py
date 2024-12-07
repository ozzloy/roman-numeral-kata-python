def parse(roman):
    value = 0
    index = 0
    while index < len(roman) and roman[index] == "I":
        index += 1
        value += 1

    if index == len(roman):
        return value

    if index == len(roman) - 1 and roman[index] == "V":
        return 5 - value

    value = 5
    index += 1
    while index < len(roman) and roman[index] == "I":
        index += 1
        value += 1

    return value
