from aoc.year2015.day5 import has_double
from aoc.year2015.day5 import has_naughty_pair
from aoc.year2015.day5 import has_repeat
from aoc.year2015.day5 import has_repeat_with_letter
from aoc.year2015.day5 import part1
from aoc.year2015.day5 import part2
import pytest

TEST_REPEAT = [
    # (test, expected)
    ("qjhvhtzxzqqjkmpb", True),
    ("xxyxx", True),
    ("uurcxstgmygtbstg", True),
    ("ieodomkazucvgmuy", False),
]

TEST_REPEAT_LETTER = [
    # (test, expected)
    ("qjhvhtzxzqqjkmpb", True),
    ("xxyxx", True),
    ("uurcxstgmygtbstg", False),
    ("ieodomkazucvgmuy", True),
]

TEST_DATA = [
    # (test, expected)
    (["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"], (2, 2))
]


TEST_PART1_DOUBLE = [
    ("ugknbfddgicrmopn", True),
    ("aaa", True),
    ("jchzalrnumimnmhp", False),
    ("haegwjzuvuyypxyu", True),
    ("dvszwmarrgswjxmb", True),
]


@pytest.mark.parametrize("test, expected", TEST_REPEAT)
def test_has_repeat(test, expected):
    assert has_repeat(test) == expected


@pytest.mark.parametrize("test, expected", TEST_REPEAT_LETTER)
def test_has_repeat_with_letter(test, expected):
    assert has_repeat_with_letter(test) == expected


@pytest.mark.parametrize("test, expected", TEST_DATA)
def test_part2(test, expected):
    assert part2(test) == expected


@pytest.mark.parametrize("test, expected", TEST_PART1_DOUBLE)
def test_has_double(test, expected):
    assert has_double(test) == expected
