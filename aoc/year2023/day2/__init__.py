from dataclasses import dataclass
import sys


@dataclass
class Dice:
    num: int
    color: str


@dataclass
class Round:
    num: int
    result: list[Dice]

    def total_dice(self) -> int:
        return sum([dice.num for dice in self.result])


@dataclass
class Game:
    num: int
    rounds: list[Round]

    def is_dice_possible(self, dice: Dice, bag: dict[str, int]) -> bool:
        if not dice.num <= bag[dice.color]:
            return False
        return True

    def is_round_possible(self, rd: Round, bag_total: int) -> bool:
        if rd.total_dice() > bag_total:
            return False
        return True

    def is_possible(self, bag: dict[str, int]) -> bool:
        bag_total = sum(dice for dice in bag.values())

        checks = []
        for rd in self.rounds:
            checks.append(self.is_round_possible(rd, bag_total))
            checks.append(all(self.is_dice_possible(dice, bag) for dice in rd.result))
        return all(checks)

    def fewest_possible(self) -> dict[str, int]:
        red = []
        green = []
        blue = []
        for rd in self.rounds:
            for dice in rd.result:
                if dice.color == "red":
                    red.append(dice.num)
                if dice.color == "green":
                    green.append(dice.num)
                if dice.color == "blue":
                    blue.append(dice.num)
        return {"red": max(red), "green": max(green), "blue": max(blue)}

    def power(self):
        game_set = self.fewest_possible()

        return game_set["red"] * game_set["blue"] * game_set["green"]


def remap_keys(ugly_dict: dict) -> dict:
    remapped_keys = {}
    for k, v in ugly_dict.items():
        if k == "num":
            remapped_keys[k] = int(v)
        else:
            remapped_keys[k] = v
    return remapped_keys


def parse_game_id(line: str) -> int:
    return int(line.split(":")[0].split()[1])


def parse_number(text: str) -> int:
    return int(text)


def parse_dice(text: str) -> Dice:
    dice = text.split()
    num = int(dice[0])
    color = dice[1]
    return Dice(num=num, color=color)


def parse_round(num: int, text: str) -> Round:
    flat_round = text.split(",")
    return Round(num=num, result=[parse_dice(d.strip()) for d in flat_round])


def parse_rounds(text: str) -> list[Round]:
    flat_rounds = text.split(":")[1]
    num_of_rounds = len(flat_rounds)
    return [parse_round(num_of_rounds, r) for r in flat_rounds.split(";")]


def parse_line(text: str) -> Game:
    game_id = parse_game_id(text)
    rounds = parse_rounds(text)

    return Game(num=game_id, rounds=rounds)


def parse_file(text: str) -> list[Game]:
    return [parse_line(line) for line in text.splitlines()]


def solve_part_1(file: str, bag: dict[str, int]):
    with open(file) as f:
        games = parse_file(f.read())
    return sum(game.num for game in games if game.is_possible(bag))


def solve_part_2(file: str):
    with open(file) as f:
        games = parse_file(f.read())
    return sum(game.power() for game in games)


def part1(file, bag):
    return solve_part_1(file, bag)


def part2(file: str):
    return solve_part_2(file)


if __name__ == "__main__":
    print(part1(".\data\input_2023_day2.txt", {"red": 12, "green": 13, "blue": 14}))
    print(part2(".\data\input_2023_day2.txt"))
