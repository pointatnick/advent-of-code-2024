import puzzle


def test_it_parses_line_into_tuple():
    assert puzzle.parse("1 3") == (1, 3)


def test_it_unzips_tuples_into_two_lists():
    assert puzzle.unzip([(1, 4), (2, 5), (3, 6)]) == ([1, 2, 3], [4, 5, 6])


def test_it_measures_distance():
    assert puzzle.measure_distance([1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 5, 9]) == 11


def test_it_records_appearances():
    assert puzzle.get_appearances([3, 3, 3, 4, 5, 9]) == {
        3: 3,
        4: 1,
        5: 1,
        9: 1,
    }


def test_it_measures_similarity():
    assert (
        puzzle.measure_similarity(
            [1, 2, 3, 3, 3, 4],
            {3: 3, 4: 1, 5: 1, 9: 1},
        )
        == 31
    )
