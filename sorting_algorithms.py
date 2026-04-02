from typing import List, Sequence, TypeVar

T = TypeVar("T")


def insertion_sort(array: Sequence[T]) -> List[T]:
    """Return a sorted copy of the input using insertion sort."""
    result = list(array)  # copy of array for out of place modification

    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result  # sorted array


def _merge(left: List[T], right: List[T]) -> List[T]:
    """Merge two sorted lists into one sorted list."""
    merged: List[T] = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def merge_sort(array: Sequence[T]) -> List[T]:
    """Return a sorted copy of the input using merge sort."""
    items = list(array)

    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left_sorted = merge_sort(items[:mid])  # sort left half
    right_sorted = merge_sort(items[mid:])  # sort right half

    return _merge(left_sorted, right_sorted)


def quick_sort(array: Sequence[T]) -> List[T]:
    """Return a sorted copy of the input using quick sort."""
    items = list(array)
    if len(items) <= 1:
        return items
    pivot = items[len(items) // 2]
    left = [x for x in items if x < pivot]
    middle = [x for x in items if x == pivot]
    right = [x for x in items if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def bubble_sort(array: Sequence[T]) -> List[T]:
    """Return a sorted copy of the input using bubble sort."""
    result = list(array)
    n = len(result)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break

    return result


def selection_sort(array: Sequence[T]) -> List[T]:
    """Return a sorted copy of the input using selection sort."""
    result = list(array)
    n = len(result)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        if min_idx != i:
            result[i], result[min_idx] = result[min_idx], result[i]

    return result
