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
    return list(map(evaluate_chunk, chunks))


def consume_values_once(values):
    if not values:
        return 0, []
    if len(values) == 1:
        return values[0], []
    first, second = values[0:2]
    if first < second:
        return second - first, values[2:]
    return first, values[1:]


def parse(roman):
    values = evaluate_chunks(chunk(roman))
    total = 0
    while values:
        value, values = consume_values_once(values)
        total += value
    return total
