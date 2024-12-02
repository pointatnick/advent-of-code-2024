def parse(line: str) -> tuple[int, int]:
    x, y = line.split()
    return (int(x), int(y))


def unzip(tuples: list[tuple[int, int]]) -> tuple[list[int], list[int]]:
    x, y = zip(*tuples)
    return list(x), list(y)


def measure_lists(first: list[int], second: list[int]) -> int:
    total = 0
    for x, y in zip(first, second):
        total += abs(x - y)
    return total


def solve():
    with open("input.txt", encoding="utf-8") as f:
        pairs = [parse(line) for line in f.readlines()]

    x, y = unzip(pairs)
    x.sort()
    y.sort()
    print(f"Distance is {measure_lists(x, y)}")


if __name__ == "__main__":
    solve()
