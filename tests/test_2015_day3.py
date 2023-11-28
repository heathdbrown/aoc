from aoc.year2015.day3 import part1, part2
import pytest

test_results = [
    (">", 2),
    ("^>v<", 4),
    ("^v^v^v^v^v", 2),
]


@pytest.mark.parametrize("directions,expected", test_results)
def test_part1(directions, expected):
    assert part1(directions) == expected
