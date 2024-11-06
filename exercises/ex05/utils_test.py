__author__ = "730822380"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_empty_list():
    """Test only_evens with an empty list."""
    assert only_evens([]) == []


def test_only_evens_mixed_numbers():
    """Test only_evens with a mixed list of odd and even numbers."""
    assert only_evens([1, 2, 3, 4, 5]) == [2, 4]


def test_only_evens_no_evens():
    """Test only_evens with a list containing only odd numbers."""
    input_list = [1, 3, 5]
    result = only_evens(input_list)
    assert result == []
    assert input_list == [1, 3, 5]


def test_sub_valid_indices():
    """Test sub function with valid start and end indices."""
    assert sub([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]


def test_sub_edge_case_full_range():
    """Test sub function with indices covering the entire list."""
    assert sub([1, 2, 3, 4, 5], 0, 5) == [1, 2, 3, 4, 5]


def test_sub_does_not_mutate_input():
    """Test that sub function does not mutate the input list."""
    original_list = [1, 2, 3, 4, 5]
    sub(original_list, 1, 3)
    assert original_list == [1, 2, 3, 4, 5]


def test_add_at_index_valid_insertion():
    """Test add_at_index with valid index to check element insertion."""
    my_list = [1, 2, 3]
    add_at_index(my_list, 4, 1)
    assert my_list == [1, 4, 2, 3]


def test_add_at_index_edge_case_end_of_list():
    """Test add_at_index with index equal to the length of the list."""
    my_list = [1, 2, 3]
    add_at_index(my_list, 4, 3)
    assert my_list == [1, 2, 3, 4]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    my_list = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(my_list, 4, 5)
