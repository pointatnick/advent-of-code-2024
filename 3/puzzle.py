import math
import re


def parse(cmd: tuple[str, str]) -> tuple[int, int]:
    return int(cmd[0]), int(cmd[1])


def parse_with_enabled(
    cmds: list[tuple[str, str, str, str]],
) -> list[tuple[int, int]]:
    enabled = True
    result = []
    for c in cmds:
        disable, enable, x, y = c
        if disable:
            enabled = False
        elif enable:
            enabled = True
        elif enabled:
            result.append((int(x), int(y)))
        else:
            result.append((0, 0))

    return result


def product(cmd: tuple[int, int]) -> int:
    return cmd[0] * cmd[1]


def solve_part_one():
    with open("input.txt", encoding="utf-8") as f:
        muls = re.findall(r"mul\((\d+),(\d+)\)", f.read())

    cmds = [parse(m) for m in muls]
    prods = [math.prod(c) for c in cmds]
    print(f"The sum of all multiplications is {sum(prods)}")


def solve_part_two():
    with open("input.txt", encoding="utf-8") as f:
        muls = re.findall(r"(don't\(\))|(do\(\))|mul\((\d+),(\d+)\)", f.read())

    cmds = parse_with_enabled(muls)
    prods = [math.prod(c) for c in cmds]
    print(f"The sum of all enabled multiplications is {sum(prods)}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
