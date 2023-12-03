from pathlib import Path

import pytest

from aoc.year2023.day1 import parse_number, solve, parse_file, str_to_num, find_prefix

TEST_DATA_DIR = Path(Path(__file__).resolve().parent / "data")

TEST_DATA = [
    # (test, expected)
    ("1abc2", 12),
    ("pqr3stu8vwx", 38),
    ("a1b2c3d4e5f", 15),
    ("treb7uchet", 77),
    ("two1nine", 29),
    ("eightwothree", 83),
    ("abcone2threexyz", 13),
    ("xtwone3four", 24),
    ("4nineeightseven2", 42),
    ("zoneight234", 14),
    ("7pqrstsixteen", 76),
]

TEST_INPUT = [
    # (test, expected)
    ("1abc2", "1abc2"),
    ("pqr3stu8vwx", "pqr3stu8vwx"),
    ("a1b2c3d4e5f", "a1b2c3d4e5f"),
    ("treb7uchet", "treb7uchet"),
    ("two1nine", "219"),
    ("eightwothree", "8wo3"),
    ("abcone2threexyz", "abc123xyz"),
    ("xtwone3four", "x2ne34"),
    ("4nineeightseven2", "49872"),
    ("zoneight234", "z1ight234"),
    ("7pqrstsixteen", "7pqrst16"),
]

TEST_PREFIX = [
    ("two1nine", ["two", "nine"]),
    ("eightwothree", ["eight", "three"]),
    ("abcone2threexyz", ["one", "three"]),
    ("xtwone3four", ["two", "four"]),
    ("4nineeightseven2", ["nine", "eight", "seven"]),
    ("zoneight234", ["one"]),
    ("7pqrstsixteen", ["sixteen"]),
]

TEST_FILE = [
    # (file, expected)
    (f"{TEST_DATA_DIR}/input_2023_day1.txt", 4),
    (f"{TEST_DATA_DIR}/input_2023_day1_part2.txt", 7),
]

TEST_SOLVE_DATA = [
    (f"{TEST_DATA_DIR}/input_2023_day1.txt", 142),
    (f"{TEST_DATA_DIR}/input_2023_day1_part2.txt", 281),
]


@pytest.mark.parametrize("test, expected", TEST_PREFIX)
def test_find_prefix(test, expected):
    assert find_prefix(test) == expected


@pytest.mark.parametrize("test, expected", TEST_INPUT)
def test_str_to_num(test, expected):
    assert str_to_num(test) == expected


@pytest.mark.parametrize("test, expected", TEST_DATA)
def test_parse_number(test, expected):
    assert parse_number(test) == expected


@pytest.mark.parametrize("file, expected", TEST_FILE)
def test_parse_file(file, expected):
    with open(file) as f:
        data = parse_file(f.read())
        assert isinstance(data, list)
        assert len(data) == expected


@pytest.mark.parametrize("file, expected", TEST_SOLVE_DATA)
def test_solve(file, expected):
    assert solve(file) == expected
