from dataclasses import dataclass
from collections import deque


@dataclass
class Card:
    num: int
    winning_numbers: list[int]
    scratched_numbers: list[int]
    instances: int = 0  # count of how many times of being selected

    def scratch_cards(self) -> int:
        return len(self.winners())

    def winners(self):
        matches = []
        for win in self.winning_numbers:
            if win in self.scratched_numbers:
                matches.append(win)
        return matches

    def points(self) -> int:
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


def parse_file(text: str, value: str = "") -> list[int] | list[Card]:
    if value == "points":
        return [parse_line(line).points() for line in text.splitlines()]
    if value == "instances":
        return [parse_line(line).instances for line in text.splitlines()]
    return [parse_line(line) for line in text.splitlines()]


def solve_part_1(file: str) -> int:
    with open(file) as f:
        cards = parse_file(f.read(), "points")
    return sum(cards)


def update_next_cards(card_list, current_card, copies):  # -> list[Any]:
    for n in range(current_card.num, current_card.num + current_card.scratch_cards()):
        # print(f"next cards: {card_list[n].num}")
        card_list[n].instances += 1
        copies.append(card_list[n])


def solve_part_2(file: str) -> int:
    with open(file) as f:
        text = f.read()
        cards = parse_file(text)
        d_cards = deque(cards)

        copies = deque()

        for card in cards:
            print(f"d_card {card.num}")
            cards[cards.index(card)].instances += 1
            update_next_cards(cards, card, copies)
            for i in range(len(copies)):
                update_next_cards(cards, copies.popleft(), copies)

            print(f"    Card Instances: {card.instances}")

        print(len(copies))

        return sum([card.instances for card in cards])


if __name__ == "__main__":
    print(solve_part_1("./data/input_2023_day4.txt"))
    print(solve_part_2("./data/input_2023_day4.txt"))
