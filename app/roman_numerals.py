from functools import reduce

values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def chunk_once(chunks, single_roman):
    if not chunks:
        return [[single_roman, 1]]
    last_chunk = chunks[-1]
    if single_roman == last_chunk[0]:
        last_chunk[1] += 1
    else:
        chunks.append([single_roman, 1])
    return chunks


def chunk(romans):
    return reduce(chunk_once, romans, [])


def evaluate_chunk(chunk):
    return values[chunk[0]] * chunk[1]


def evaluate_chunks(chunks):
    return [1]


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
    if roman[0] == "X":
        return 10 + parse(roman[1:])
    return values[roman[0]] + (len(roman) - 1)
