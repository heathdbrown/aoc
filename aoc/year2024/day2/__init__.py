reports = []
with open("./data/input_2024_day2.txt") as f:
    for line in f.readlines():
        reports.append([int(z) for z in line.split()])

safe_count = 0

for report in reports:
    n = len(report)
    safe_count += (all(1 <= report[i + 1] - report[i] <= 3 for i in range(n - 1))) or (
        all(1 <= report[i] - report[i + 1] <= 3 for i in range(n - 1))
    )

print(safe_count)
