from dataclasses import dataclass
from collections import Counter
from enum import Enum

card_rank = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "1": 1,
}


class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 6
    FIVE_OF_A_KIND = 7


@dataclass
class Hand:
    bid: int
    cards: str
    rank: int = 0
    type: HandType | None = None

    def card_count(self) -> Counter[str]:
        return Counter(self.cards)

    def card_values(self) -> list[int]:
        return [card_rank[card] for card in self.cards]

    def set_type(self):
        card_count = self.card_count()

        most_common = card_count.most_common()

        if most_common[0][1] == 5:
            self.type = HandType.FIVE_OF_A_KIND

        if most_common[0][1] == 4:
            self.type = HandType.FOUR_OF_A_KIND

        if most_common[0][1] == 3:
            if most_common[1][1] == 2:
                self.type = HandType.FULL_HOUSE
            else:
                self.type = HandType.THREE_OF_A_KIND

        if most_common[0][1] == 2:
            if most_common[1][1] == 2:
                self.type = HandType.TWO_PAIR
            else:
                self.type = HandType.ONE_PAIR

        if most_common[0][1] == 1:
            self.type = HandType.HIGH_CARD

        return self.type

    def set_rank(self, index: int) -> int:
        self.rank = index + 1
        return self.rank

    def rank_up(self):
        self.rank += 1
        return self.rank

    def rank_down(self):
        self.rank -= 1
        return self.rank


def rank(index: int, hand: Hand, sorted_hands: list[Hand]):
    rank_up = []
    if index + 1 < len(sorted_hands):
        if hand.type == sorted_hands[index + 1].type:
            for card1, card2 in zip(hand.cards, sorted_hands[index + 1].cards):
                if card_rank[card1] == card_rank[card2]:
                    rank_up.append(0)
                elif card_rank[card1] < card_rank[card2]:
                    rank_up.append(-1)
                elif card_rank[card1] > card_rank[card2]:
                    rank_up.append(1)
    return rank_up


def hand_type(hand: Hand) -> int:
    return hand.type.value


def parse_bid(text: str) -> int:
    return int(text.split()[1].strip())


def parse_hand(text: str) -> str:
    return text.split()[0].strip()


def parse_line(text: str):
    return Hand(bid=parse_bid(text), cards=parse_hand(text))


def parse_file(text: str):
    return [parse_line(line) for line in text.splitlines()]


def card_sort(hand: Hand):
    return hand.card_values()


def solve_part_1(file: str):
    with open(file) as f:
        hands = parse_file(f.read())

        for hand in hands:
            hand.set_type()

        hands.sort(key=hand_type)

        # sorted_hands = sorted(hands, key=hand_type)

        # for hand in hands:
        #     print(hand.type, hand.cards, hand.card_values())

        high_cards = [hand for hand in hands if hand.type == HandType.HIGH_CARD]
        high_cards.sort(key=card_sort)

        one_pair = [hand for hand in hands if hand.type == HandType.ONE_PAIR]
        one_pair.sort(key=card_sort)
        # print(len(one_pair))

        two_pair = [hand for hand in hands if hand.type == HandType.TWO_PAIR]
        two_pair.sort(key=card_sort)
        # print(two_pair)

        three_of_a_kind = [
            hand for hand in hands if hand.type == HandType.THREE_OF_A_KIND
        ]
        three_of_a_kind.sort(key=card_sort)
        # print(three_of_a_kind)

        four_of_a_kind = [
            hand for hand in hands if hand.type == HandType.FOUR_OF_A_KIND
        ]
        four_of_a_kind.sort(key=card_sort)
        # print(four_of_a_kind)

        full_house = [hand for hand in hands if hand.type == HandType.FULL_HOUSE]
        full_house.sort(key=card_sort)
        # print(full_house)

        five_of_a_kind = [
            hand for hand in hands if hand.type == HandType.FIVE_OF_A_KIND
        ]
        five_of_a_kind.sort(key=card_sort)
        # print(five_of_a_kind)

        combined = [
            *high_cards,
            *one_pair,
            *two_pair,
            *three_of_a_kind,
            *full_house,
            *four_of_a_kind,
            *five_of_a_kind,
        ]

        for idx, hand in enumerate(combined):
            hand.set_rank(idx)
            # print(hand.rank)

        return sum([hand.bid * hand.rank for hand in combined])

        # for idx, hand in enumerate(sorted_hands):
        #     hand.set_rank(idx)

        # for hand in sorted_hands:
        #     print(hand.cards, hand.type, hand.rank)

        ## Passes tests but is HIGH for the final answer
        # for idx, hand in enumerate(sorted_hands):
        #     if idx + 1 < len(sorted_hands):
        #         current_hand = hand
        #         next_hand = sorted_hands[idx + 1]
        #         if current_hand.type == next_hand.type:
        #             # print(current_hand.cards, next_hand.cards)
        #             combined = zip(current_hand.cards, next_hand.cards)
        #             rank_change = None
        #             for card1, card2 in combined:
        #                 card1_val = card_rank[card1]
        #                 card2_val = card_rank[card2]
        #                 card_diff = card1_val - card2_val
        #                 # print(card1, card1_val, card2, card2_val, card_diff)
        #                 if card_diff > 0:
        #                     rank_change = True
        #                     break

        #                 if card_diff < 0:
        #                     rank_change = False
        #                     break
        #             if rank_change:
        #                 current_hand.rank_up()
        #                 next_hand.rank_down()

        # total = []
        # for hand in sorted_hands:
        #     # print(hand.cards, hand.type, hand.rank)
        #     total.append(hand.bid * hand.rank)

        # return sum(total)


def solve_part_2(file: str):
    with open(file) as f:
        hands = parse_file(f.read())


if __name__ == "__main__":
    print("Part 1: ", solve_part_1("./data/input_2023_day7.txt"))
    print("Part 2: ", solve_part_2("./data/input_2023_day7.txt"))
