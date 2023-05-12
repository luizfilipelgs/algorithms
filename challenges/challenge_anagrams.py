from typing import Tuple


def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    left, right = [], []

    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


def is_anagram(first_string: str, second_string: str) -> Tuple[str, str, bool]:
    first_sorted = ''.join(quick_sort(list(first_string.lower())))
    second_sorted = ''.join(quick_sort(list(second_string.lower())))

    if not first_string or not second_string:
        return first_sorted, second_sorted, False

    if len(first_string) != len(second_string):
        return first_sorted, second_sorted, False

    return first_sorted, second_sorted, first_sorted == second_sorted
