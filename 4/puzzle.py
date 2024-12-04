def count(word: str) -> int:
    num = 0
    for i in range(0, len(word) - 3):
        if word[i : i + 4] == "XMAS" or word[i : i + 4] == "SAMX":
            num += 1
    return num


def count_two(word: str) -> int:
    num = 0
    for i in range(0, len(word) - 2):
        if word[i : i + 3] == "MAS" or word[i : i + 3] == "SAM":
            num += 1
    return num


def extract_vertical(words: list[str], idx: int) -> str:
    return "".join([w[idx] for w in words])


def extract_lr_diagonal(words: list[str], x: int, y: int) -> str:
    pos_x, pos_y = (x, y)
    result: list[str] = []
    while True:
        try:
            result.append(words[pos_y][pos_x])
            pos_x += 1
            pos_y += 1
        except IndexError:
            break
    return "".join(result)


def extract_rl_diagonal(words: list[str], x: int, y: int) -> str:
    pos_x, pos_y = (x, y)
    result: list[str] = []
    while True:
        try:
            result.append(words[pos_y][pos_x])
            pos_x -= 1
            if pos_x < 0:
                break
            pos_y += 1
        except IndexError:
            break
    return "".join(result)


def count_xmas(words: list[str]) -> int:
    h_count = sum([count(w) for w in words])
    verticals = [extract_vertical(words, x) for x in range(0, len(words))]
    v_count = sum([count(w) for w in verticals])
    lr_diagonals = [extract_lr_diagonal(words, 0, y) for y in range(0, len(words) - 3)] + [
        extract_lr_diagonal(words, x, 0) for x in range(1, len(words) - 3)
    ]
    lrd_count = sum([count(w) for w in lr_diagonals])
    rl_diagonals = [extract_rl_diagonal(words, len(words) - 1, y) for y in range(0, len(words) - 3)] + [
        extract_rl_diagonal(words, x, 0) for x in range(len(words) - 2, 3, -1)
    ]
    rld_count = sum([count(w) for w in rl_diagonals])
    return h_count + v_count + lrd_count + rld_count


def count_x_mas(words: list[str]) -> int:
    num = 0
    for y in range(1, len(words)):
        for x in range(1, len(words)):
            if words[y][x] == "A":
                try:
                    if (
                        words[y - 1][x - 1] == "M"
                        and words[y + 1][x + 1] == "S"
                        or words[y - 1][x - 1] == "S"
                        and words[y + 1][x + 1] == "M"
                    ) and (
                        words[y - 1][x + 1] == "M"
                        and words[y + 1][x - 1] == "S"
                        or words[y - 1][x + 1] == "S"
                        and words[y + 1][x - 1] == "M"
                    ):
                        num += 1
                except IndexError:
                    continue

    return num


def solve_part_one():
    with open("input.txt", encoding="utf-8") as f:
        lines = f.readlines()
        print(f"XMAS appears {count_xmas(lines)} times")


def solve_part_two():
    with open("input.txt", encoding="utf-8") as f:
        lines = f.readlines()
        print(f"X-MAS appears {count_x_mas(lines)} times")


if __name__ == "__main__":
    solve_part_one()
    solve_part_two()
