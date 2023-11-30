import pytest
from parse import Result

from aoc.year2015.day7 import process_line

TEST_PROCESS_LINE = [
    # (test, expected)
    ("123 -> x", ("assignment", {"signal": "123", "wire": "x"})),
    ("456 -> y", ("assignment", {"signal": "456", "wire": "y"})),
    ("x AND y -> d", ("and", {"wire_a": "x", "wire_b": "y", "wire": "d"})),
    ("x OR y -> e", ("or", {"wire_a": "x", "wire_b": "y", "wire": "e"})),
    ("x LSHIFT 2 -> f", ("lshift", {"wire_a": "x", "bit": "2", "wire": "f"})),
    ("y RSHIFT 2 -> g", ("rshift", {"wire_a": "y", "bit": "2", "wire": "g"})),
    ("NOT x -> h", ("not", {"wire_a": "x", "wire": "h"})),
    ("NOT y -> i", ("not", {"wire_a": "y", "wire": "i"})),
]

TEST_DATA = [
    # (test, expected)
    (
        [
            "123 -> x",
            "456 -> y",
            "x AND y -> d",
        ],
        {"d": 72},
    ),
    (
        [
            "123 -> x",
            "456 -> y",
            "x OR y -> e",
        ],
        {"e": 507},
    ),
    (
        [
            "123 -> x",
            "456 -> y",
            "x LSHIFT 2 -> f",
        ],
        {"f": 492},
    ),
    (
        [
            "123 -> x",
            "456 -> y",
            "y RSHIFT 2 -> g",
        ],
        {"g": 114},
    ),
    (
        [
            "123 -> x",
            "456 -> y",
            "NOT x -> h",
        ],
        {"h": 65412},
    ),
    (
        [
            "123 -> x",
            "456 -> y",
            "NOT y -> i",
        ],
        {"i": 65079},
    ),
    (
        [
            "123 -> x",
        ],
        {"x": 123},
    ),
    (
        [
            "456 -> y",
        ],
        {"y": 456},
    ),
]


@pytest.mark.parametrize("test, expected", TEST_PROCESS_LINE)
def test_process_line(test, expected):
    assert process_line(test) == expected
