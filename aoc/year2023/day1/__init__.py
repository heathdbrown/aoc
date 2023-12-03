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
    digits = []
    for char in text:
        if char.isdigit():
            digits.append(char)
    if len(digits) == 2:
        return int("".join(digits))
    if len(digits) > 2:
        num: str = "".join(digits)
        first = num[0]
        last = num[-1:]
        return int(first + last)
    if len(digits) == 1:
        return int("".join(digits) * 2)
    if len(digits) == 0:
        return 0


def parse_file(text: str) -> list[int]:
    return [parse_number(line) for line in text.splitlines()]


def find_prefix(text: str):
    return re.findall(
        "one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen",
        text,
    )


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


if __name__ == "__main__":
    print(part1("./data/input_2023_day1.txt"))
