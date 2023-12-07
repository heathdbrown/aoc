from dataclasses import dataclass


@dataclass
class Race:
    num: int
    time: int
    record: int
    ways_to_beat: int


def multiply_list(iterable: list) -> int:
    total = 1
    for element in iterable:
        total = total * element

    return total


def ways_to_beat_record(time: int, record: int) -> int:
    distance = 0
    hold_time = 0

    ways = []
    for i in range(1, record + 1):
        # do racing
        travel_time = time - hold_time
        distance = travel_time * hold_time
        if distance > record:
            ways.append(hold_time)
        hold_time += 1

    return len(ways)


def parse_record(text: str) -> list[int]:
    return [int(n) for n in text.split("\n")[1].split(":")[1].strip().split()]


def parse_time(text: str) -> list[int]:
    return [int(n) for n in text.split("\n")[0].split(":")[1].strip().split()]


def parse_line(text: str) -> list[Race]:
    times = parse_time(text)
    records = parse_record(text)
    combined = zip(times, records)

    races = []
    count = 0
    for time, record in combined:
        count += 1
        ways = ways_to_beat_record(time, record)
        races.append(Race(num=count, time=time, record=record, ways_to_beat=ways))

    return races


def parse_record_2(text: str) -> int:
    return int("".join([n for n in text.split("\n")[1].split(":")[1].strip().split()]))


def parse_time_2(text: str) -> int:
    return int("".join([n for n in text.split("\n")[0].split(":")[1].strip().split()]))


def parse_line_2(text: str) -> int:
    time = parse_time_2(text)
    record = parse_time_2(text)

    ways = ways_to_beat_record(time, record)

    return ways


def parse_file(text: str) -> list[Race]:
    return parse_line(text)


def parse_file_2(text: str) -> int:
    return parse_line_2(text)


def solve_part_1(file):
    with open(file) as f:
        races = parse_file(f.read())

        total = 1
        for race in races:
            total = total * race.ways_to_beat

    return total


def solve_part_2(file):
    with open(file) as f:
        races = parse_file_2(f.read())

    return races


if __name__ == "__main__":
    print(solve_part_1("./data/input_2023_day6.txt"))
    print(solve_part_2("./data/input_2023_day6.txt"))
