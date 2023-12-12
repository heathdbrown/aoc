import re


from aoc.utils import sliding_window

prefix = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "teen": "10",
    "eleven": "11",
    "twelve": "12",
    "thirteen": "13",
    "fourteen": "14",
    "fifteen": "15",
    "sixteen": "16",
    "seventeen": "17",
    "eighteen": "18",
    "nineteen": "19",
}

suffix = {"teen": 10}


def parse_number(text: str):
    # digits = []
    # for char in text:
    #     if char.isdigit():
    #         digits.append(char)
    # if len(digits) == 2:
    #     return int("".join(digits))
    # if len(digits) > 2:
    #     num: str = "".join(digits)
    #     first = num[0]
    #     last = num[-1:]
    #     return int(first + last)
    # if len(digits) == 1:
    #     return int("".join(digits) * 2)
    # if len(digits) == 0:
    #     return 0
    p1 = 0
    p2 = 0
    p1_digits = []
    p2_digits = []
    for i, c in enumerate(text):
        if c.isdigit():
            p1_digits.append(c)
            p2_digits.append(c)
        for d, val in enumerate(
            ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        ):
            if text[i:].startswith(val):
                p2_digits.append(str(d + 1))
        # p1 += int(p1_digits[0] + p1_digits[-1])
        p2 += int(p2_digits[0] + p2_digits[-1])
    return p1, p2


def parse_file(text: str) -> list[tuple[int, int]]:
    return [parse_number(line) for line in text.splitlines()]


def find_prefix(text: str):
    # return re.findall(
    #     "one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen",
    #     text,
    # )
    ...


def str_to_num(text: str):
    prefixes = find_prefix(text)

    if "teen" in prefixes:
        "".join(prefixes)

    output = text
    for i, val in enumerate(prefixes):
        output = re.sub(val, prefix[val], output)

    return "".join(output)


def solve(data: str):
    with open(data) as f:
        nums = parse_file(f.read())
    return sum(nums)


def part1(file_path: str):
    return solve(file_path)


def part2(file_path: str):
    with open(file_path) as f:
        text = f.read().strip()
    lines = text.splitlines()
    # https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/1.py
    p1 = 0
    p2 = 0
    for line in lines:
        p1_digits = []
        p2_digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                p1_digits.append(c)
                p2_digits.append(c)
            for d, val in enumerate(
                ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
            ):
                if line[i:].startswith(val):
                    p2_digits.append(str(d + 1))
        # p1 += int(p1_digits[0] + p1_digits[-1])
        p2 += int(p2_digits[0] + p2_digits[-1])
    return p2


if __name__ == "__main__":
    # print(part1("./data/input_2023_day1.txt"))
    print(part2("./data/input_2023_day1.txt"))
