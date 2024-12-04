import puzzle


def test_it_counts_xmas():
    assert (
        puzzle.count_xmas(
            [
                "MMMSXXMASM",
                "MSAMXMSMSA",
                "AMXSXMAAMM",
                "MSAMASMSMX",
                "XMASAMXAMM",
                "XXAMMXXAMA",
                "SMSMSASXSS",
                "SAXAMASAAA",
                "MAMMMXMMMM",
                "MXMXAXMASX",
            ]
        )
        == 18
    )


def test_it_counts_one_string():
    assert puzzle.count("XMASAMXAMM") == 2


def test_it_extracts_a_vertical_string():
    assert (
        puzzle.extract_vertical(
            [
                "MMMSXXMASM",
                "MSAMXMSMSA",
                "AMXSXMAAMM",
                "MSAMASMSMX",
                "XMASAMXAMM",
                "XXAMMXXAMA",
                "SMSMSASXSS",
                "SAXAMASAAA",
                "MAMMMXMMMM",
                "MXMXAXMASX",
            ],
            0,
        )
        == "MMAMXXSSMM"
    )


def test_it_extracts_a_lr_diagonal_string():
    assert (
        puzzle.extract_lr_diagonal(
            [
                "MMMSXXMASM",
                "MSAMXMSMSA",
                "AMXSXMAAMM",
                "MSAMASMSMX",
                "XMASAMXAMM",
                "XXAMMXXAMA",
                "SMSMSASXSS",
                "SAXAMASAAA",
                "MAMMMXMMMM",
                "MXMXAXMASX",
            ],
            0,
            0,
        )
        == "MSXMAXSAMX"
    )


def test_it_extracts_a_rl_diagonal_string():
    assert (
        puzzle.extract_rl_diagonal(
            [
                "MMMSXXMASM",
                "MSAMXMSMSA",
                "AMXSXMAAMM",
                "MSAMASMSMX",
                "XMASAMXAMM",
                "XXAMMXXAMA",
                "SMSMSASXSS",
                "SAXAMASAAA",
                "MAMMMXMMMM",
                "MXMXAXMASX",
            ],
            9,
            0,
        )
        == "MSAMMMMXAM"
    )


def test_it_counts_x_mas():
    assert (
        puzzle.count_x_mas(
            [
                "MMMSXXMASM",
                "MSAMXMSMSA",
                "AMXSXMAAMM",
                "MSAMASMSMX",
                "XMASAMXAMM",
                "XXAMMXXAMA",
                "SMSMSASXSS",
                "SAXAMASAAA",
                "MAMMMXMMMM",
                "MXMXAXMASX",
            ]
        )
        == 9
    )
