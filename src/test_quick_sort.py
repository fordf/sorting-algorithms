"""Tests for quick sort function."""
import pytest
from random import randint


LISTS = [
    ([1.11111], [1.11111]),
    ([], []),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([4, 2, 4, 1, 3, 5, 6, 3], [1, 2, 3, 3, 4, 4, 5, 6]),
    ([-1, -10, -3, 2, 139, -101, 192], [-101, -10, -3, -1, 2, 139, 192]),
    ([3.3, 1.12, 42, 19.999999, 19.999], [1.12, 3.3, 19.999, 19.999999, 42]),
    (['aa', 'b', 'a', 'ab'], ['a', 'aa', 'ab', 'b']),
]


@pytest.mark.parametrize('unsorted_lst, sorted_lst', LISTS)
def test_quick_sort(unsorted_lst, sorted_lst):
    """Quick sort should sort lists."""
    from quick_sort import quick_sort
    assert quick_sort(unsorted_lst) == sorted_lst


def test_quick_sort_against_python_sort():
    """Test quick sort against python's sort method."""
    from quick_sort import quick_sort
    input_list = [randint(0, 100000) for i in range(1000)]
    test_list = quick_sort(input_list)
    input_list.sort()
    assert test_list == input_list
