__author__ = "730822380"

from find_max import find_and_remove_max


def test_normal_find_and_remove_max() -> None:
    test_list = [3, 5, 7, 9]
    assert find_and_remove_max(test_list) == 9


def test_mutation() -> None:
    test_list = [1, 8, 2, 3, 3]
    find_and_remove_max(test_list)
    assert test_list == [1, 2, 3, 3]


def test_edge_case() -> None:
    test_list = [-9, -5, -2, -2]
    assert find_and_remove_max(test_list) == -2
    assert test_list == [-9, -5, -2]
