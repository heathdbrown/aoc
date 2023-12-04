import pytest
from pathlib import Path

from aoc.year2023.day3 import solve_part_1, parse_line, parse_file, parse_pos
from aoc.year2023.day3 import Number

TEST_DATA_DIR = Path(Path(__file__).resolve().parent / "data")


def test_parse_pos():
    text = "467..114.."
    response = ["467", "114"]
    assert parse_pos(text, response[0]) == (0, 3)
    assert parse_pos(text, response[1]) == (5, 8)


def test_parse_line():
    text = "467..114.."

    assert parse_line(text, 0) == {
        "467": Number(name="467", position=(0, 3), linenum=0),
        "114": Number(name="114", position=(5, 8), linenum=0),
    }


def test_parse_file():
    with open(f"{TEST_DATA_DIR}/input_2023_day3.txt") as f:
        text = parse_file(f.read())

        assert isinstance(text, list) is True
        assert len(text) == 10


def test_solve_part_1():
    assert solve_part_1(f"{TEST_DATA_DIR}/input_2023_day3.txt") == 4361
