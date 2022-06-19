def two_sum(array, k):
    """
    Returns any pair from the array that sums up to the number k, otherwise returns empty list.

    Complexity is O(n).
    Memory O(n).

    """
    hashtable = {i: k - i for i in array}
    for i in array:
        if i in hashtable.values():
            if [i, hashtable[i]]:
                return [i, hashtable[i]]
    return []


def two_sum_in_sorted_array(array, k):
    """
    Returns any pair from the sorted array that sums up to the number k,
    otherwise returns empty list.

    Algorithm is binary search.

    Complexity is O(n*log(n))
    Memory O(1)

    """
    for i in array:
        number_to_find = k - i
        left = 0
        right = len(array) - 1
        while left <= right:
            middle = int((left + right) / 2)
            if array[middle] == number_to_find:
                return [i, number_to_find]
            elif array[middle] > number_to_find:
                right = middle - 1
            else:
                left = middle + 1
    return []


def two_sum_optimal_in_sorted_array(array, k):
    """
    Returns any pair from the sorted array that sums up to the number k,
    otherwise returns empty list.

    Complexity is O(n).
    Memory O(1).

    """
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] + array[right] == k:
            return [array[left], array[right]]
        elif array[left] + array[right] < k:
            left += 1
        elif array[left] + array[right] > k:
            right -= 1
    return []


if __name__ == '__main__':
    print(two_sum([-3, 5, 7, 5, 4, 5, 6, 0], 7))
    print(two_sum_in_sorted_array(sorted([-3, 5, 7, 5, 4, 5, 6, 0]), 7))
    print(two_sum_optimal_in_sorted_array(sorted([-3, 5, 7, 5, 4, 5, 6, 0]), 7))