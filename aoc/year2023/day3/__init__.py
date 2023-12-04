from dataclasses import dataclass
import re
import string


@dataclass
class Number:
    name: str
    position: tuple
    linenum: int
    line_count: int = 0

    def next_line(self) -> int:
        if self.linenum + 1 == self.line_count:
            return self.linenum
        return self.linenum + 1

    def prev_line(self) -> int:
        if self.linenum == 0:
            return self.linenum
        return self.linenum - 1

    def start(self) -> int:
        return self.position[0]

    def stop(self) -> int:
        return self.position[1]


def parse_pos(text: str, response: str) -> tuple[int, int]:
    start = text.find(response)
    stop = start + len(response)
    return (start, stop)


def parse_line(text: str, line_num: int, line_count: int) -> dict[str, Number]:
    number = re.compile(r"(\d+)")
    resp = number.findall(text)

    positions = {}
    for num in resp:
        positions[num] = Number(
            name=num,
            position=parse_pos(text, num),
            linenum=line_num,
            line_count=line_count,
        )

    return positions


def parse_file(text: str):
    return [
        parse_line(line, line_num, text.splitlines())
        for line_num, line in enumerate(text.splitlines())
    ]


def check_symbols(text: str) -> bool:
    not_symbols = "."
    if not_symbols in text:
        return False
    return True


def parse_symbols(text: str) -> list[str]:
    not_symbols = "."
    symbols = []
    for idx, char in enumerate(text):
        if all((not_symbols != char, char not in string.digits)):
            symbols.append(idx)
    return symbols


def solve_part_1(file: str):
    with open(file) as f:
        data = f.read()
        numbers = parse_file(data)

        lines = data.splitlines()

        verified_numbers = []
        for idx, line in enumerate(lines):
            for lookup in numbers:
                for number in lookup.values():
                    if idx == number.linenum:
                        # check_next_line_pos for symbols
                        if idx + 1 < len(lines):
                            if idx == 0:
                                prev_line = line
                            else:
                                prev_line = lines[idx - 1]
                            next_line = lines[idx + 1]
                            start, stop = number.position
                            next_val = stop
                            prev_symbols = parse_symbols(prev_line)
                            symbols = parse_symbols(line)
                            next_symbols = parse_symbols(next_line)
                            print(f"Previous found {idx}, {symbols}")
                            print(f"Symbols found {idx}, {symbols}")
                            print(f"Next Symbols {next_symbols}")
                            print(f"Lookup: {line[start:stop]}")
                            print(f"Line: {line}")
                            print(f"Next Line: {next_line}")
                            print(f"{number.position}")
                            if start == 0:
                                print(f"Next Value Same line: {line[stop]}")
                                print(
                                    f"Next line, adjacent: {next_line[stop]}",
                                    stop,
                                )
                                print(f"Next line below: {next_line[start:stop]}")
                                if any(
                                    [
                                        check_symbols(line[stop]),
                                        check_symbols(next_line[stop]),
                                        check_symbols(next_line[start:stop]),
                                    ]
                                ):
                                    verified_numbers.append(int(number.name))
                            elif start > 0 and stop + 1 < len(line):
                                if idx - 1 == -1:
                                    print("you are the top line")
                                print(f"Previous line: {prev_line}")
                                print(f"Previous value Same line: {line[start - 1]}")
                                print(f"Next Value Same line: {line[stop]}")
                                print(
                                    f"Next line, previous adjacent: {next_line[start-1]}"
                                )
                                print(f"Next line, adjacent: {next_line[stop]}")
                                if check_symbols(line[start - 1 : stop + 1]):
                                    print(line[start - 1 : stop + 1])
                                    verified_numbers.append(int(number.name))
                                elif check_symbols(next_line[start - 1 : stop + 1]):
                                    verified_numbers.append(int(number.name))
        return verified_numbers


if __name__ == "__main__":
    print(solve_part_1("./tests/data/input_2023_day3.txt"))
