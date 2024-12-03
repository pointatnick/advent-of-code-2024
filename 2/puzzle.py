def parse(line: str) -> list[int]:
    return [int(x) for x in line.split()]


def is_increasing(list: list[int]) -> bool:
    for x in range(0, len(list) - 1):
        if list[x] >= list[x + 1]:
            return False
    return True


def is_decreasing(list: list[int]) -> bool:
    for x in range(0, len(list) - 1):
        if list[x] <= list[x + 1]:
            return False
    return True


def is_safe_difference(list: list[int]) -> bool:
    for x in range(0, len(list) - 1):
        diff = abs(list[x] - list[x + 1])
        if diff < 1 or diff > 3:
            return False
    return True


def dampen(list: list[int]) -> list[list[int]]:
    lists = []
    for x in range(0, len(list)):
        lists.append(list[:x] + list[x + 1 :])
    return lists


def solve_part_one():
    with open("input.txt", encoding="utf-8") as f:
        reports = [parse(line) for line in f.readlines()]

    num_safe_reports = 0
    for r in reports:
        if is_safe_difference(r) and (is_increasing(r) or is_decreasing(r)):
            num_safe_reports += 1

    print(f"There are {num_safe_reports} safe reports")


def solve_part_two():
    with open("input.txt", encoding="utf-8") as f:
        reports = [parse(line) for line in f.readlines()]

    num_safe_reports = 0
    for r in reports:
        drs = dampen(r)
        for dr in drs:
            if is_safe_difference(dr) and (is_increasing(dr) or is_decreasing(dr)):
                num_safe_reports += 1
                break

    print(f"There are {num_safe_reports} dampened safe reports")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
