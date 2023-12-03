from pathlib import Path
import pytest

from aoc.year2023.day2 import solve_part_1
from aoc.year2023.day2 import solve_part_2
from aoc.year2023.day2 import parse_file
from aoc.year2023.day2 import parse_line
from aoc.year2023.day2 import parse_dice
from aoc.year2023.day2 import Dice, Round, Game
from aoc.year2023.day2 import parse_dice, parse_file, parse_round, parse_rounds

TEST_DATA_DIR = Path(Path(__file__).resolve().parent / "data")

TEST_FILE = [
    # (file, expected)
    (f"{TEST_DATA_DIR}/input_2023_day2_part1.txt", 5),
    # (f"{TEST_DATA_DIR}/input_2023_day2_part1.txt", 5),
]

TEST_FILES = [
    (
        f"{TEST_DATA_DIR}/input_2023_day2_part1.txt",
        {"red": 12, "green": 13, "blue": 14},
        8,
    )
]


def test_parse_dice():
    assert parse_dice("1 red".strip()) == Dice(num=1, color="red")


def test_parse_round():
    text = "3 blue, 4 red"
    assert isinstance(parse_round(1, text), Round)


def test_parse_rounds():
    text = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    assert isinstance(parse_rounds(text), list)
    assert len(parse_rounds(text)) == 3


def test_parse_line():
    text = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    assert isinstance(parse_line(text), Game)


def test_fewest_possible():
    text = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    game = parse_line(text)
    assert game.fewest_possible() == {"red": 4, "green": 2, "blue": 6}


def test_power():
    text = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    game = parse_line(text)
    assert game.power() == 48


@pytest.mark.parametrize("file, expected", TEST_FILE)
def test_parse_file(file, expected):
    with open(file) as f:
        text = parse_file(f.read())

        assert isinstance(text, list) is True
        assert len(text) == expected


@pytest.mark.parametrize("file, bag, expected", TEST_FILES)
def test_solve_part_1(file, bag, expected):
    assert solve_part_1(file, bag) == expected


def test_solve_part_2():
    assert solve_part_2(f"{TEST_DATA_DIR}/input_2023_day2_part1.txt") == 2286
