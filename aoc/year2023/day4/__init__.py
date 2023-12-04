from dataclasses import dataclass


@dataclass
class Card:
    num: int
    winning_numbers: list[int]
    scratched_numbers: list[int]

    def winners(self):
        matches = []
        for win in self.winning_numbers:
            if win in self.scratched_numbers:
                matches.append(win)
        return matches

    def points(self):
        matches = self.winners()

        if len(matches) == 0:
            return 0

        score = 0
        for idx, i in enumerate(matches):
            if idx == 0:
                score += 1
            else:
                score += score
        return score


def parse_scratched_numbers(text: str) -> list[int]:
    return [int(num) for num in text.split(":")[1].split("|")[1].split()]


def parse_winning_numbers(text: str) -> list[int]:
    return [int(num) for num in text.split(":")[1].split("|")[0].split()]


def parse_card(text: str) -> Card:
    return Card(
        int(text.split(":")[0].split()[1]),
        parse_winning_numbers(text),
        parse_scratched_numbers(text),
    )


def parse_line(text: str) -> Card:
    return parse_card(text)


def parse_file(text: str) -> list[int]:
    return [parse_line(line).points() for line in text.splitlines()]


def solve_part_1(file: str) -> int:
    with open(file) as f:
        cards = parse_file(f.read())
    return sum(cards)


if __name__ == "__main__":
    print(solve_part_1("./data/input_2023_day4.txt"))
