from app.roman_numerals import parse


def test_roman_numeral_parser():
    assert parse("IX") == 9
