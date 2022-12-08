def read_input_raw(file: str) -> str:
    with open(file, "r") as f:
        data = f.read()
    return data


def read_input_splitlines(file: str) -> list[str]:
    with open(file, "r") as f:
        data = f.read().splitlines()
    return data
