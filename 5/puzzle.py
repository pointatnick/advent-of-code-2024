import re


def parse_order(line: str) -> dict[int, int]:
    first, second = line.split("|")
    return {int(first): int(second)}


def parse_update(line: str) -> list[int]:
    return [int(x) for x in line.split(",")]


def merge_orders(orders: list[dict[int, int]]) -> dict[int, list[int]]:
    result: dict[int, list[int]] = {}
    for o in orders:
        for k, v in o.items():
            if k in result:
                result[k].append(v)
            else:
                result[k] = [v]
    return result


def get_orders_for_update(update: list[int], orders: dict[int, list[int]]) -> dict[int, list[int]]:
    result: dict[int, list[int]] = {}
    for x in range(1, len(update)):
        if update[x] in orders:
            result[update[x]] = orders[update[x]]
    return result


def is_valid(ints: list[int], orders: dict[int, list[int]]) -> bool:
    if not orders or not ints:
        return True
    last = ints[-1]
    rest = ints[:-1]
    if last in orders:
        for r in rest:
            if r in orders[last]:
                return False
        orders.pop(last)
    return is_valid(rest, orders)


def reorder(ints: list[int], orders: dict[int, list[int]]) -> list[int]:
    x = len(ints) - 1
    while not is_valid(ints, orders.copy()):
        last = ints[x]
        rest = ints[:x]
        if last in orders:
            for r in rest:
                if r in orders[last]:
                    ints.pop(x)
                    ints.insert(0, last)
                    break
            x -= 1
        else:
            x -= 1
        if x == 0:
            x = len(ints) - 1
    return ints


def midpoint(ints: list[int]) -> int:
    return ints[len(ints) // 2]


def solve_part_one():
    with open("input.txt", encoding="utf-8") as f:
        content = f.read()
    orders = merge_orders([parse_order(line) for line in re.findall(r"^.*\|.*", content, flags=re.MULTILINE)])
    updates = [parse_update(line) for line in re.findall(r"^.*,.*", content, flags=re.MULTILINE)]
    valid_updates = [u for u in updates if is_valid(u, get_orders_for_update(u, orders))]
    result = sum([midpoint(u) for u in valid_updates])
    print(f"The sum of middle page numbers is {result}")


def solve_part_two():
    with open("input.txt", encoding="utf-8") as f:
        content = f.read()
    orders = merge_orders([parse_order(line) for line in re.findall(r"^.*\|.*", content, flags=re.MULTILINE)])
    updates = [parse_update(line) for line in re.findall(r"^.*,.*", content, flags=re.MULTILINE)]
    invalid_updates = [u for u in updates if not is_valid(u, get_orders_for_update(u, orders))]
    ordered_updates = [reorder(u, orders) for u in invalid_updates]
    result = sum([midpoint(u) for u in ordered_updates])
    print(f"The sum of re-ordered middle page numbers is {result}")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
