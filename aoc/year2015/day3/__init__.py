from aoc.utils import read_input_raw
from dataclasses import dataclass

# data = read_input_raw("tests\test_2015_day3.txt")
data = read_input_raw("data\input_2015_day3.txt")


@dataclass
class Location:
    x = 0
    y = 0
    prev_x = 0
    prev_y = 0

    def update_location(self, x, y):
        self.prev_x = self.x
        self.prev_y = self.y
        self.x += x
        self.y += y
        return self.current_location()

    def current_location(self) -> tuple[int, int]:
        return self.x, self.y

    def previous_location(self) -> tuple[int, int]:
        return self.prev_x, self.prev_y


"""
north (^), south (v), east (>), or west (<)

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
"""
direction_map = {
    "^": {"x": 1, "y": 0},
    ">": {"x": 0, "y": 1},
    "v": {"x": -1, "y": 0},
    "<": {"x": 0, "y": -1},
}


def part1(data):
    location = Location()
    directions_l = list(data)
    locations = []
    for d in directions_l:
        locations.append(location.current_location())
        location.update_location(direction_map[d]["x"], direction_map[d]["y"])
        locations.append(location.current_location())

    return len(set(locations))


def part2(data):
    santa_location = Location()
    robot_location = Location()
    directions_l = list(data)
    locations = []
    for idx, d in enumerate(directions_l):
        print(idx, d)
        if idx == 0:
            locations.append(santa_location.current_location())
            locations.append(robot_location.current_location())
        if idx % 2:
            locations.append(santa_location.current_location())
            santa_location.update_location(direction_map[d]["x"], direction_map[d]["y"])
            locations.append(santa_location.current_location())
        else:
            locations.append(robot_location.current_location())
            robot_location.update_location(direction_map[d]["x"], direction_map[d]["y"])
            locations.append(robot_location.current_location())
    return len(set(locations))


if __name__ == "__main__":
    print("Houses for part1:", part1(data))
    print("Part2: ", part2(data))
