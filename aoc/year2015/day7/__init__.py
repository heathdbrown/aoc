from dataclasses import dataclass

import parse
from parse import Result, Match

from aoc.utils import read_input_splitlines

parse_dict = {
    "and": parse.Parser("{wire_a} AND {wire_b} -> {wire}"),
    "or": parse.Parser("{wire_a} OR {wire_b} -> {wire}"),
    "lshift": parse.Parser("{wire_a} LSHIFT {bit} -> {wire}"),
    "rshift": parse.Parser("{wire_a} RSHIFT {bit} -> {wire}"),
    "not": parse.Parser("NOT {wire_a} -> {wire}"),
    "assignment": parse.Parser("{signal} -> {wire}"),
}


# def process_line(text: str):
#     compiler = parse.Parser("{signal:d} -> {wire:l}")
#     parse_result = compiler.parse(text)
#     return parse_result.named if parse_result else {}


@dataclass
class Wire:
    name: str
    signal: int


def process_line(text: str):
    for key, parser in parse_dict.items():
        match_ = parser.parse(text)
        if match_:
            if key == "assignment":
                return (
                    key,
                    Wire(name=match_.named["name"], signal=int(match_.named["signal"])),
                )
            if key == "and":
                return (key,)
    return None, None


def process_instructions(instructions: list[tuple[str, dict] | tuple[None, None]]):
    wires = []
    for operator, instruction in instructions:
        if operator == "assignment":
            wires.append(
                Wire(
                    name=instruction.get("wire"), signal=int(instruction.get("signal"))
                )
            )

    return wires


def read_file(name: str) -> list[tuple[str, dict] | tuple[None, None]]:
    with open(name, "r", encoding="utf8") as f:
        results = process_instructions([process_line(line.strip()) for line in f])
    return results


def b_and(x: int, y: int) -> int:
    return x & y


def b_or(x: int, y: int) -> int:
    return x | y


def b_right(x: int, y: int) -> int:
    return x >> y


def b_left(x: int, y: int) -> int:
    return x << y


def b_complement(x: int) -> int:
    return ~x


def provide(signal: int) -> int:
    return signal


def part1(data):
    pass


def part2(data):
    pass


if __name__ == "__main__":
    print(part1("./data/input_2015_day7.txt"))
    print(part2("./data/input_2015_day7.txt"))
