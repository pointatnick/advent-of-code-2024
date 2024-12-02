import puzzle


def test_it_parses_line_into_tuple():
    assert puzzle.parse("1 3") == (1, 3)


def test_it_unzips_tuples_into_two_lists():
    assert puzzle.unzip([(1, 4), (2, 5), (3, 6)]) == ([1, 2, 3], [4, 5, 6])


def test_it_compares_numbers_and_sums_distance():
    assert puzzle.measure_lists([1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 5, 9]) == 11
