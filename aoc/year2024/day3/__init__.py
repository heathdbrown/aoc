# https://www.youtube.com/watch?v=GSSjIIaa3Cs
import re

with open("./data/input_2024_day3.txt", "r") as f:
    data = f.read()


pattern = r"mul\(\d+,\d+\)"


def get_result(s):
    result = 0
    for m in re.findall(pattern, s):
        l, r = m.split(",")
        result += int(l[4:]) * int(r[:-1])
    return result


print("Part 1: ", get_result(data))

clean_data = []
i = 0
do = True

while i < len(data):
    if do:
        if data[i : i + 7] == "don't()":
            do = False
            i += 7
        else:
            clean_data.append(data[i])
            i += 1
    else:
        if data[i : i + 4] == "do()" and data[i : i + 7] != "don't()":
            do = True
            i += 4
        else:
            i += 1

clean_data = "".join(clean_data)
print("Part 2: ", get_result(clean_data))
