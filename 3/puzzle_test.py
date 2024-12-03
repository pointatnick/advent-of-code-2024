import puzzle


def test_it_parses_mul_cmd():
    assert puzzle.parse(("2", "5")) == (2, 5)


def test_it_parses_with_enabled():
    assert puzzle.parse_with_enabled(
        [
            ("", "", "1", "2"),
            ("", "do()", "", ""),
            ("", "", "3", "4"),
            ("don't()", "", "", ""),
            ("", "", "4", "2"),
        ]
    ) == [(1, 2), (3, 4), (0, 0)]
