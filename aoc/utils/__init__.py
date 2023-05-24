import collections
from itertools import islice

def read_input_raw(file: str) -> str:
    with open(file, "r") as f:
        data = f.read()
    return data


def read_input_splitlines(file: str) -> list[str]:
    with open(file, "r") as f:
        data = f.read().splitlines()
    return data

def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)