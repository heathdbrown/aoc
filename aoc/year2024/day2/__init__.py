import collections
from itertools import islice


def read_file(filename):
    with open(filename, "r") as f:
        data = f.readlines()
    return data


def sliding_window(iterable, n):
    "Collect data into overlapping fixed-length chunks or blocks."
    # sliding_window('ABCDEFG', 4) → ABCD BCDE CDEF DEFG
    iterator = iter(iterable)
    window = collections.deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)


def increasing_trend(nums: list[int]) -> bool:
    if not (sorted(nums) == nums):
        return False
    return True


def decreasing_trend(nums: list[int]) -> bool:
    if not (sorted(nums, reverse=True) == nums):
        return False
    return True


def part1():
    # data = read_file("./tests/data/input_2024_day2.txt")
    data = read_file("./data/input_2024_day2.txt")

    data = [[int(l) for l in i.strip().split()] for i in data]

    answer = {}
    safe = 0
    unsafe = 0
    for k, report in enumerate(data):
        n = len(report)
        r = {}
        diffs = []
        diffs_check = []
        if increasing_trend(report) or decreasing_trend(report):
            r["trend"] = True
        else:
            r["trend"] = False
        for i in range(n):
            if i + 1 < n:
                diff = abs(report[i] - report[i + 1])
                diffs.append(diff)
                if diff == 0:
                    diffs_check.append(False)
                elif diff > 3:
                    diffs_check.append(False)
                else:
                    diffs_check.append(True)
        # r["diffs"] = diffs
        r["diffs_check"] = all(diffs_check)
        answer[k + 1] = all(r.values())
        if answer[k + 1] is True:
            safe += 1
        if answer[k + 1] is False:
            unsafe += 1
    return safe


def part2():
    data = read_file("./tests/data/input_2024_day2.txt")

    # data = read_file("./data/input_2024_day2.txt")

    data = [[int(l) for l in i.strip().split()] for i in data]
    answer = {}
    safe = 0
    unsafe = 0
    for k, report in enumerate(data):
        n = len(report)
        r = {}
        diffs = []
        diffs_check = []
        if increasing_trend(report) or decreasing_trend(report):
            r["trend"] = True
        else:
            r["trend"] = False
        for i in range(n):
            if i + 1 < n:
                diff = abs(report[i] - report[i + 1])
                diffs.append(diff)
                if diff == 0:
                    diffs_check.append(False)
                elif diff > 3:
                    diffs_check.append(False)
                else:
                    diffs_check.append(True)
        # r["diffs"] = diffs

        r["diffs_check"] = all(diffs_check)
        c = collections.Counter(diffs_check)
        if c[False] == 1:
            r["single_value"] = True
        else:
            r["single_value"] = False
        answer[k + 1] = r
        if answer[k + 1]["trend"] is True and answer[k + 1]["diffs_check"] is True:
            safe += 1
        if answer[k + 1]["trend"] is False and answer[k + 1]["single_value"] is True:
            safe += 1
    return answer, safe


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
