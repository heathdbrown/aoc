from aoc.utils import read_input_splitlines
from collections import Counter
from collections import deque
from itertools import islice
from itertools import pairwise
import re
import string

data = read_input_splitlines("./data/input_2015_day5.txt")


def has_vowels(s):
    count = Counter(s)
    vowels = ("a", "i", "e", "o", "u")
    vowel_count = []
    for l in vowels:
        if count.get(l):
            vowel_count.append(count.get(l))

    return sum(vowel_count) >= 3


def has_double(s):
    double_letters = [f"{l}{l}" for l in string.ascii_lowercase]
    pairs = ["".join(pair) for pair in pairwise(s)]
    check = []
    for pair in pairs:
        if pair not in double_letters:
            check.append(False)
        else:
            check.append(True)
    return any(check)


def has_naughty_pair(s):
    naughty_pair = ("ab", "cd", "pq", "xy")
    check = []
    for pair in pairwise(s):
        if "".join(pair) in naughty_pair:
            check.append(True)
        else:
            check.append(False)
    return any(check)


def part1(data):
    nice = []
    naughty = []
    for s in data:
        if has_naughty_pair(s):
            naughty.append(s)
            continue
        if has_double(s) and has_vowels(s):
            nice.append(s)
        else:
            naughty.append(s)

    return len(nice), len(naughty)


def has_repeat(s):
    # my attempt
    # kept getting '59'
    # pairs = [pair for pair in pairwise(s)]
    # count = Counter(pairs)

    # check = []
    # for c in count.values():
    #     if c >= 2:
    #         check.append(True)
    #     else:
    #         check.append(False)
    # return any(check)

    # correct is 55
    if not re.search(r"(.)(.).*\1\2", s):  # some wild boobies appear
        return False
    return True


# def sliding_window(iterable, n):
#     # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
#     it = iter(iterable)
#     window = deque(islice(it, n - 1), maxlen=n)
#     for x in it:
#         window.append(x)
#         yield tuple(window)


def has_repeat_with_letter(s):
    # my attempt
    # kept getting '59'
    # patterns = list(sliding_window(s, 3))

    # check = []
    # for pattern in patterns:
    #     if pattern[0] == pattern[len(pattern) - 1]:
    #         if not pattern[0] == pattern[0 + 1]:
    #             check.append(pattern)
    # return any(check)

    # correct is 55
    if not re.search(r"(.).\1", s):
        return False
    return True


def part2(data):
    # https://www.reddit.com/r/adventofcode/comments/3viazx/day_5_solutions/
    nice = []
    naughty = []
    for s in data:
        if all((has_repeat(s), has_repeat_with_letter(s))):
            nice.append(s)
        else:
            naughty.append(s)
    return len(nice), len(naughty)


if __name__ == "__main__":
    print("Part1: ", part1(data))
    print("Part2: ", part2(data))
