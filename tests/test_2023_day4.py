import pytest
from pathlib import Path

from aoc.year2023.day4 import Card
from aoc.year2023.day4 import parse_card
from aoc.year2023.day4 import parse_winning_numbers
from aoc.year2023.day4 import parse_scratched_numbers
from aoc.year2023.day4 import parse_line
from aoc.year2023.day4 import parse_file
from aoc.year2023.day4 import solve_part_1

TEST_DATA_DIR = Path(Path(__file__).resolve().parent / "data")

TEST_DATA = [
    # (text, expected)
    ("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", 8),
    ("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", 2),
    ("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", 2),
    ("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", 1),
    ("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", 0),
    ("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", 0),
]


def winners():
    text = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    card = parse_card(text)
    assert card.winners() == [48, 83, 86, 17]


@pytest.mark.parametrize("text, expected", TEST_DATA)
def points(text, expected):
    card = parse_card(text)
    assert card.points() == expected


def test_parse_scratched_numbers():
    text = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    assert parse_scratched_numbers(text) == [83, 86, 6, 31, 17, 9, 48, 53]


def test_parse_winning_numbers():
    text = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    assert parse_winning_numbers(text) == [41, 48, 83, 86, 17]


def test_parse_card():
    text = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    assert parse_card(text) == Card(
        num=1,
        winning_numbers=[41, 48, 83, 86, 17],
        scratched_numbers=[83, 86, 6, 31, 17, 9, 48, 53],
    )


@pytest.mark.parametrize("text, expected", TEST_DATA)
def test_parse_line(text, expected):
    assert parse_line(text).points() == expected


def test_solve():
    assert solve_part_1(f"{TEST_DATA_DIR}/input_2023_day4.txt") == 13
