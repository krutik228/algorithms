
def the_largest_range_in_array(array):
    """
    Find the largest range in array

    For instance, the output for array [9, 28, 2, 3, 4, 5] is [2, 5]
    Elements may not be adjacent, for example, output for [2, 5, 28, 4, 9, 3, 2] is [2, 5]

    """
    numbers = {x: 0 for x in array}
    left = right = 0

    for number in numbers:
        if numbers[number] == 0:
            left_count = number - 1
            right_count = number + 1

            while left_count in numbers:
                numbers[left_count] = 1
                left_count -= 1
            left_count += 1

            while right_count in numbers:
                numbers[right_count] = 1
                right_count += 1
            right_count -= 1

            if (right - left) <= (right_count -left_count):
                right = right_count
                left = left_count
    return [left, right]


if __name__ == '__main__':
    print(the_largest_range_in_array([11, 7, 3, 1, 2, 2, 0]))



