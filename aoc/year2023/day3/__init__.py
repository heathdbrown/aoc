from dataclasses import dataclass
import re
import string


@dataclass
class Number:
    name: str
    position: tuple
    linenum: int
    line_count: int = 0
    line_length: int = 0

    def number(self) -> int:
        """Convert the name string to a 'int'

            examples: '419' = 419

        Returns:
            int: name string converted
        """
        return int(self.name)

    def next_line(self) -> int:
        """Next line based on the line number that the was found on

            examples:
                linenum = 0; next_line=1
                linenum = line_count+1; next_line = line_count

        Returns:
            int: index of the next line number
        """
        if self.linenum + 1 == self.line_count:
            return self.linenum
        return self.linenum + 1

    def prev_line(self) -> int:
        """Previous line based on the line number that the Number was found on

            examples:
                linenum = 0; prev_line = 0
                linenum = 1; prev_line = 0

        Returns:
            int: index of the previous line number
        """
        if self.linenum == 0:
            return self.linenum
        return self.linenum - 1

    def start(self) -> int:
        """Start or 'beginning' position of the number

            example: text[start:3]

        Returns:
            int: start position
        """
        return self.position[0]

    def stop(self) -> int:
        """Stop or 'end' position of the number

            example: text[0:stop]

        Returns:
            int: stop position
        """
        return self.position[1]

    def next(self) -> int:
        """Next value index of the value following the 'stop' position

        Returns:
            int: index of the next value
        """
        if self.stop() == self.line_length:
            return self.stop()
        return self.stop() + 1

    def prev(self) -> int:
        """Previous value index of the value following the 'start' position

        Returns:
            int: index of the prev value
        """
        if self.start() == 0:
            return self.start()
        return self.start() - 1

    def line_index(self) -> list[int]:
        return list(range(self.start(), self.stop()))

    def prev_index(self) -> list[int]:
        return list(range(self.prev(), self.next()))

    def next_index(self) -> list[int]:
        return list(range(self.prev(), self.next()))


def parse_pos(text: str, response: str) -> tuple[int, int]:
    start = text.find(response)
    stop = start + len(response)
    return (start, stop)


def parse_line(text: str, line_num: int, line_count: int) -> dict[str, Number]:
    line_length = len(text)

    number = re.compile(r"(\d+)")
    resp = number.findall(text)

    positions = {}
    for num in resp:
        positions[num] = Number(
            name=num,
            position=parse_pos(text, num),
            linenum=line_num,
            line_count=line_count,
            line_length=line_length,
        )

    return positions


def parse_file(text: str) -> list[dict[str, Number]]:
    return [
        parse_line(line, line_num, len(text.splitlines()))
        for line_num, line in enumerate(text.splitlines())
    ]


def check_symbols(text: str) -> bool:
    not_symbols = "."
    if not_symbols in text:
        return False
    return True


def check_symbols_index(symbol_indexes: list[int], line_indexes: list[int]) -> bool:
    return any(symbol in line_indexes for symbol in symbol_indexes)


def parse_symbols(text: str) -> list[int]:
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

        verified_numbers = []
        lines = data.splitlines()
        for num in numbers:
            for number in num.values():
                print(number.number())
                print(number.prev_line())
                print(
                    number.linenum, lines[number.linenum][number.prev() : number.next()]
                )
                print(number.next_line())
                current_line_symbols = parse_symbols(lines[number.linenum])
                print(f"current line symbols index: {current_line_symbols}")
                next_line_symbols = parse_symbols(lines[number.next_line()])
                print(f"next line symbols index: {next_line_symbols}")
                prev_line_symbols = parse_symbols(lines[number.prev_line()])
                print(f"previous line symbols index: {prev_line_symbols}")
                if number.linenum == 0:
                    print(f"Check line 0")
                    if any(
                        (
                            check_symbols_index(
                                current_line_symbols, number.line_index()
                            ),
                            check_symbols_index(next_line_symbols, number.line_index()),
                        )
                    ):
                        print(f"Found Symbols for: {number.number()}")
                        verified_numbers.append(number.number())

                elif number.linenum == number.line_count:
                    if any(
                        (
                            check_symbols_index(
                                current_line_symbols, number.line_index()
                            ),
                            check_symbols_index(prev_line_symbols, number.line_index()),
                        )
                    ):
                        verified_numbers.append(number.number())
                elif number.linenum not in (0, number.line_count):
                    if any(
                        (
                            check_symbols_index(
                                current_line_symbols, number.line_index()
                            ),
                            check_symbols_index(next_line_symbols, number.line_index()),
                            check_symbols_index(prev_line_symbols, number.line_index()),
                        )
                    ):
                        verified_numbers.append(number.number())
        return verified_numbers


if __name__ == "__main__":
    print(solve_part_1("./tests/data/input_2023_day3.txt"))
