def read_file(filename):
    with open(filename, "r") as f:
        data = f.read().splitlines()
    return data


def part1():
    data = read_file("./data/input_2024_day3.txt")

    import re

    m = re.compile(r"(mul\(\d+,\d+\))")

    found = []
    for line in data:
        matches = re.findall(m, line)
        found.append(matches)

    solution = []
    for f in found:
        for m in f:
            a, b = m.strip("mul").strip("(").strip(")").split(",")
            sol = int(a) * int(b)
            solution.append(sol)

    return sum(solution)


def part2():
    data = read_file("./data/input_2024_day3.txt")

    import re

    m = re.compile(r"(don\'t\(\))|(do\(\))|(mul\(\d+\,\d+\))")

    found = []
    for line in data:
        matches = re.findall(m, line)
        found.append([matches])

    t = {}
    for f in found:
        for m in f:
            for i, p in enumerate(m):
                start, stop, mul = p[0], p[1], p[2]
                if start:
                    t[i] = "start"
                if stop:
                    t[i] = "stop"
                if mul:
                    a, b = mul.strip("mul").strip("(").strip(")").split(",")
                    t[i] = int(a) * int(b)
    commands: list[dict[int, str]] = []
    for k, v in t.items():
        if not isinstance(v, int):
            commands.append({k: v})

    # have the 'indexes' 'keys' for the start and stop commands
    # have the multipliers


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: ")
    part2()
