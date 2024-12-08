import pytest
from app.roman_numerals import (
    parse,
    chunk,
    chunk_once,
    evaluate_chunk,
    evaluate_chunks,
    consume_values_once,
)

I = "I"
V = "V"


@pytest.mark.parametrize(
    "chunks,single_roman,expected",
    [
        ([], I, [[I, 1]]),
        ([[I, 1]], I, [[I, 2]]),
        ([[I, 1]], V, [[I, 1], [V, 1]]),
    ],
)
def test_chunk_once(chunks, single_roman, expected):
    assert chunk_once(chunks, single_roman) == expected


@pytest.mark.parametrize(
    "romans,expected",
    [(I, [[I, 1]]), (I + I, [[I, 2]]), (I + V, [[I, 1], [V, 1]])],
)
def test_chunk(romans, expected):
    assert chunk(romans) == expected


@pytest.mark.parametrize(
    "chunk,expected",
    [([I, 1], 1), ([I, 2], 2), ([V, 1], 5), ([V, 2], 10)],
)
def test_evaluate_chunk(chunk, expected):
    assert evaluate_chunk(chunk) == expected


@pytest.mark.parametrize(
    "chunks,expected",
    [([[I, 1]], [1]), ([[I, 2]], [2]), ([[I, 1], [V, 1]], [1, 5])],
)
def test_evaluate_chunks(chunks, expected):
    assert evaluate_chunks(chunks) == expected


@pytest.mark.parametrize(
    "values,expected",
    [
        ([1], (1, [])),
        ([1, 5], (4, [])),
        ([5], (5, [])),
        ([5, 1], (5, [1])),
    ],
)
def test_consume_values_once(values, expected):
    assert consume_values_once(values) == expected


@pytest.mark.parametrize(
    "roman,expected",
    [
        ("IX", 9),
        ("X", 10),
        ("XI", 11),
        ("XIV", 14),
        ("XV", 15),
        ("XVI", 16),
        ("XIX", 19),
        ("XX", 20),
        ("XXV", 25),
        ("XXXIV", 34),
        ("XLI", 41),
        ("MCMLXXXIV", 1984),
        ("MCMXCIX", 1999),
    ],
)
def test_roman_numeral_parser(roman, expected):
    assert parse(roman) == expected
