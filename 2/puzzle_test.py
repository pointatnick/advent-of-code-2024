import puzzle


def test_it_parses_the_input():
    assert puzzle.parse("7 6 4 2 1") == [7, 6, 4, 2, 1]


def test_it_checks_if_list_is_increasing():
    assert puzzle.is_increasing([1, 3, 6, 7, 9]) is True
    assert puzzle.is_increasing([7, 6, 4, 2, 1]) is False


def test_it_checks_if_list_is_decreasing():
    assert puzzle.is_decreasing([1, 3, 6, 7, 9]) is False
    assert puzzle.is_decreasing([7, 6, 4, 2, 1]) is True


def test_it_checks_if_list_differs_enough():
    assert puzzle.is_safe_difference([7, 6, 4, 2, 1]) is True
    assert puzzle.is_safe_difference([1, 2, 7, 8, 9]) is False
