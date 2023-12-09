import pytest
from pathlib import Path

from aoc.year2023.day7 import (
    parse_bid,
    parse_file,
    parse_hand,
    parse_line,
    solve_part_1,
    Hand,
)

TEST_DATA_DIR = Path(Path(__file__).resolve().parent / "data")


@pytest.fixture
def input_file():
    with open(f"{TEST_DATA_DIR}/input_2023_day7.txt") as f:
        data = f.read()
    return data


def test_parse_bind():
    text = "32T3K 765"
    assert parse_bid(text) == 765


def test_parse_hand():
    text = "32T3K 765"
    assert parse_hand(text) == "32T3K"


def test_parse_line():
    text = "32T3K 765"
    assert parse_line(text) == Hand(rank=0, bid=765, cards="32T3K")


def test_parse_file(input_file):
    assert isinstance(parse_file(input_file), list) == True
    assert len(parse_file(input_file)) == 5


def test_solve_part_1():
    assert solve_part_1(f"{TEST_DATA_DIR}/input_2023_day7.txt") == 6440
