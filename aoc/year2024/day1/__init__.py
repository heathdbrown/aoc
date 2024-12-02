from collections import defaultdict


def read_file(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.read().split("\n")
    return data


def part1():
    data = read_file("./data/input_2024_day1.txt")
    # data = read_file("./tests/data/input_2024_day1.txt")
    distances = []
    list1 = []
    list2 = []
    for l in data:
        if len(l) == 0:
            break
        list1.append(int(l.split()[0]))
        list2.append(int(l.split()[1]))

    list1.sort()
    list2.sort()

    pairs = []
    for i in range(len(list1)):
        pairs.append((list1.pop(), list2.pop()))

    for p in pairs:
        distances.append(abs(p[0] - p[1]))

    print(sum(distances))


def part2():
    data = read_file("./data/input_2024_day1.txt")
    # data = read_file("./tests/data/input_2024_day1.txt")

    similarity = defaultdict(int)
    list1 = []
    list2 = []
    for l in data:
        if len(l) == 0:
            break
        list1.append(int(l.split()[0]))
        list2.append(int(l.split()[1]))

    for i in list1:
        if i not in similarity:
            similarity[i] = i * list2.count(i)
        else:
            similarity[i] += i * list2.count(i)

    print(sum(similarity.values()))


if __name__ == "__main__":
    print("Part 1: ")
    part1()
    print("Part2: ")
    part2()
