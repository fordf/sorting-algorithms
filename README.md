[![Build Status](https://travis-ci.org/fordf/sorting-algorithms.svg?branch=radix)](https://travis-ci.org/fordf/sorting-algorithms)

# Sorting Algorithms

## Radix Sort
Put each number into a bucket corresponding to it's least significant digit. For example,
247 would go into bucket 7. Take your buckets (a list of lists), and flatten it, then repeat
for the next-most least significant digit. For 247 that'd be 4.

Module: [radix_sort](https://github.com/fordf/sorting-algorithms/blob/insertion/src/radix_sort.py)

Time Complexity:
* best-case: O(kn)
* average-case: O(kn)
* worst-case: O(kn)
where k is the number of digits in the biggest number

## Merge Sort
Take an unsorted list, recursively slice list segments in half until each item is
on it's own.
```
[4, 2, 8, 1]
 |
 V
[4, 2] [8, 1]
 |
 V
[4] [2]  [8] [1]
```
Go back up stack trace, merging pairs of list segments in sorted order.
```
[4] [2]  [8] [1]
 |
 V
[2, 4] [1, 8]
 |
 V
[1, 2, 4, 8]
```

Module: [merge_sort](https://github.com/fordf/sorting-algorithms/blob/merge/src/merge_sort.py)

Time Complexity:
* best-case: O(n*log(n))
* average-case: O(n*log(n))
* worst-case: O(n*log(n))

## Insertion Sort
For each element in the given list, compare it's value to the previous elements one
at a time. If the current element is smaller than the previous element, swap them,
and compare against the new previous element. Once the previous element is smaller
than the current element, continue on to the next unsorted element.

Module: [insertion_sort](https://github.com/fordf/sorting-algorithms/blob/insertion/src/insertion_sort.py)

Time Complexity: 
* best-case: O(n)
* average-case: O(n<sup>2</sup>)
* worst-case: O(n<sup>2</sup>)



