import pytest
from pathlib import Path

from aoc.year2023.day6 import Race
from aoc.year2023.day6 import ways_to_beat_record
from aoc.year2023.day6 import parse_record
from aoc.year2023.day6 import parse_time
from aoc.year2023.day6 import parse_line
from aoc.year2023.day6 import parse_file
from aoc.year2023.day6 import solve_part_1
from aoc.year2023.day6 import solve_part_2


TEST_DATA_DIR = Path(Path(__file__).resolve().parent / "data")


@pytest.fixture
def input_file():
    with open(f"{TEST_DATA_DIR}/input_2023_day6.txt") as f:
        data = f.read()
    return data


TEST_TIME_AND_DISTANCE = [
    # (time, record, expected)
    (7, 9, 4),
    (15, 40, 8),
    (30, 200, 9),
]


@pytest.mark.parametrize("time, record, expected", TEST_TIME_AND_DISTANCE)
def test_ways_to_beat_record(time, record, expected):
    # time = 7
    # record = 9

    assert ways_to_beat_record(time, record) == expected


def test_parse_record():
    text = "Time:      7  15   30\nDistance:  9  40  200"
    assert parse_record(text) == [9, 40, 200]


def test_parse_time():
    text = "Time:      7  15   30\nDistance:  9  40  200"
    assert parse_time(text) == [7, 15, 30]


def test_parse_line(input_file):
    text = "Time:      7  15   30\nDistance:  9  40  200"
    assert parse_line(text) == [
        Race(num=1, time=7, record=9, ways_to_beat=4),
        Race(num=2, time=15, record=40, ways_to_beat=8),
        Race(num=3, time=30, record=200, ways_to_beat=9),
    ]


def test_parse_file(input_file):
    assert len(parse_file(input_file)) == 3
    assert isinstance(parse_file(input_file), list)


def test_solve_part_1():
    assert solve_part_1(f"{TEST_DATA_DIR}/input_2023_day6.txt") == 288


def test_solve_part_2():
    assert solve_part_2(f"{TEST_DATA_DIR}/input_2023_day6.txt") == 71503
