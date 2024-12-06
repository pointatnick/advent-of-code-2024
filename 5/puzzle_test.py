import puzzle


def test_it_parses_sort_order():
    assert puzzle.parse_order("75|53") == {75: 53}


def test_it_parses_page_update():
    assert puzzle.parse_update("75,47,61,53,29") == [75, 47, 61, 53, 29]


def test_it_merges_sort_orders():
    assert puzzle.merge_orders([{91: 88}, {92: 39}, {92: 57}]) == {91: [88], 92: [39, 57]}


def test_it_gets_orders_for_update():
    assert puzzle.get_orders_for_update([75, 29, 13], {75: [1], 29: [13]}) == {29: [13]}


def test_it_checks_for_valid_updates():
    assert puzzle.is_valid([75, 29, 13], {29: [13]}) is True
    assert puzzle.is_valid([75, 29, 13], {29: [75]}) is False


def test_it_reorders_update():
    assert puzzle.reorder(
        [75, 97, 47, 61, 53],
        {75: [29, 53, 47, 61, 13], 97: [13, 61, 47, 29, 53, 75], 47: [53, 13, 61, 29], 61: [13, 53, 29], 53: [29, 13]},
    ) == [97, 75, 47, 61, 53]
    assert puzzle.reorder([61, 13, 29], {61: [13, 53, 29], 29: [13]}) == [61, 29, 13]
    assert puzzle.reorder(
        [97, 13, 75, 29, 47],
        {75: [29, 53, 47, 61, 13], 97: [13, 61, 47, 29, 53, 75], 47: [53, 13, 61, 29], 29: [13]},
    ) == [97, 75, 47, 29, 13]


def test_it_returns_middle_page():
    assert puzzle.midpoint([75, 29, 13]) == 29
