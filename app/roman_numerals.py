def parse(roman):
    values = {
        "V": 5,
        "X": 10,
    }
    if not roman:
        return 0
    if roman[0] == "I":
        if roman[-1] == "I":
            return len(roman)
        return values[roman[-1]] - (len(roman) - 1)
    return values[roman[0]] + (len(roman) - 1)
