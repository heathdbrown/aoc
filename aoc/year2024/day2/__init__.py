reports = []
with open("./data/input_2024_day2.txt") as f:
    for line in f.readlines():
        reports.append([int(z) for z in line.split()])


def is_safe(l):
    n = len(l)
    return (all(1 <= l[i + 1] - l[i] <= 3 for i in range(n - 1))) or (
        all(1 <= l[i] - l[i + 1] <= 3 for i in range(n - 1))
    )


safe_count = sum(map(is_safe, reports))

print(safe_count)
