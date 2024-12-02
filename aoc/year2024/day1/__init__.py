from collections import defaultdict
from collections import Counter


def read_file(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()
    return data


def part1():
    data = read_file("./data/input_2024_day1.txt")
    # data = read_file("./tests/data/input_2024_day1.txt")

    a, b = [], []
    for line in data:
        x, y = (int(z) for z in line.split())
        a.append(x)
        b.append(y)
    a.sort()
    b.sort()
    n = len(a)
    print(sum(abs(a[i] - b[i]) for i in range(n)))


def part2():
    data = read_file("./data/input_2024_day1.txt")
    # data = read_file("./tests/data/input_2024_day1.txt")

    a, b = [], []
    for line in data:
        x, y = (int(z) for z in line.split())
        a.append(x)
        b.append(y)

    n = len(a)
    c = Counter(b)

    print(sum(a[i] * c[a[i]] for i in range(n)))


if __name__ == "__main__":
    print("Part 1: ")
    part1()
    print("Part2: ")
    part2()
