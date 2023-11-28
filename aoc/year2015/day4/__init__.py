import hashlib


def part1(key):
    for num in range(100_000_000):
        test = key + str(num)
        encoded_test = test.encode()
        md5_hash = hashlib.md5(encoded_test).hexdigest()
        if md5_hash[0:5] == "00000":
            return num


def part2(key):
    for num in range(100_000_000):
        test = key + str(num)
        encoded_test = test.encode()
        md5_hash = hashlib.md5(encoded_test).hexdigest()
        if md5_hash[0:6] == "000000":
            return num


if __name__ == "__main__":
    print("Part 1:", part1("ckczppom"))
    print("Part 2:", part2("ckczppom"))
