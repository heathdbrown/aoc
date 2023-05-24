from aoc.utils import read_input_raw


data = read_input_raw("data\input_2015_day2.txt")

lines = data.splitlines()


def surface_area(length: int, width: int, height: int) -> int:
    return 2 * ((length * width) + (width * height) + (height * length))


def smallest_side(length: int, width: int, height: int) -> int:
    return min([length * width, width * height, height * length])


def perimeter(x: int, y: int) -> int:
    return 2 * (x + y)


def ribbon_length(length: int, width: int, height: int):
    sides = [
        perimeter(length, width),
        perimeter(width, height),
        perimeter(length, height),
    ]
    return min(sides)


def ribbon_volume(length: int, width: int, height: int) -> int:
    return length * width * height


def part1(lines):
    total_paper = []
    for line in lines:
        l, w, h = line.split("x")
        total_paper.append(surface_area(int(l), int(w), int(h)))
        total_paper.append(smallest_side(int(l), int(w), int(h)))
    return sum(total_paper)


def part2(lines):
    total_ribbon = []
    for line in lines:
        l, w, h = line.split("x")
        total_ribbon.append(ribbon_volume(int(l), int(w), int(h)))
        total_ribbon.append(ribbon_length(int(l), int(w), int(h)))
    return sum(total_ribbon)
