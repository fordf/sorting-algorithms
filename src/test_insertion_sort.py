"""Tests for insertion sort function."""
import pytest

LISTS = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([4, 2, 4, 1, 3, 5, 6, 3], [1, 2, 3, 3, 4, 4, 5, 6]),
    ([-1, -10, -3, 2, 139, -101, 192], [-101, -10, -3, -1, 2, 139, 192]),
    (['aa', 'b', 'a', 'ab'], ['a', 'aa', 'ab', 'b']),
]


@pytest.mark.parametrize('unsorted_lst, sorted_lst', LISTS)
def test_insertion_sort(unsorted_lst, sorted_lst):
    """."""
    from insertion_sort import insertion_sort
    assert insertion_sort(unsorted_lst) == sorted_lst
