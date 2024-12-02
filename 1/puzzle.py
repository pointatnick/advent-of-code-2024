def parse(line: str) -> tuple[int, int]:
    x, y = line.split()
    return (int(x), int(y))


def unzip(tuples: list[tuple[int, int]]) -> tuple[list[int], list[int]]:
    x, y = zip(*tuples)
    return list(x), list(y)


def measure_distance(first: list[int], second: list[int]) -> int:
    """Measures the distance between two lists, both sorted in ascending order.
    Distance is the absolute value between a number in one list and its
    corresponding number in the same index in the other list.
    """
    total = 0
    for x, y in zip(first, second):
        total += abs(x - y)
    return total


def get_appearances(list: list[int]) -> dict[int, int]:
    apps = {}
    for x in list:
        if x in apps:
            apps[x] += 1
        else:
            apps[x] = 1
    return apps


def measure_similarity(list: list[int], appearances: dict[int, int]) -> int:
    """Measures the similarity of a list. Similarity is the product of a number
    in the first list multiplied by the number of times it appears in the
    appearance dict.
    """
    total = 0
    for x in list:
        total += x * appearances.get(x, 0)
    return total


def solve_part_one():
    with open("input.txt", encoding="utf-8") as f:
        pairs = [parse(line) for line in f.readlines()]

    x, y = unzip(pairs)
    x.sort()
    y.sort()
    print(f"Distance is {measure_distance(x, y)}")


def solve_part_two():
    with open("input.txt", encoding="utf-8") as f:
        pairs = [parse(line) for line in f.readlines()]

    x, y = unzip(pairs)
    x.sort()
    apps = get_appearances(y)
    print(f"Similarity score is {measure_similarity(x, apps)}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
