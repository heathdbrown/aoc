from itertools import accumulate
from aoc.utils import read_input_raw


directions = {"(": 1, ")": -1}

floors = read_input_raw("data/input_2015_day1.txt")


def part1(floors):
    return sum(directions[floor] for floor in floors)


def part2(floors):
    for idx, v in enumerate(accumulate(directions[floor] for floor in floors)):
        if v == -1:
            return idx


if __name__ == "__main__":
    print(part1(floors))
    print(part2(floors))
