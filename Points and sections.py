from bisect import bisect_left, bisect_right
import random

def quick_sort(A, left, right):
    if left >= right:
        return
    fst, lst = partition(A, left, right)
    quick_sort(A, left, lst)
    quick_sort(A, fst, right)

def partition(A, left, right):
    pivot = A[random.randint(left, right)]
    i, j = left, right
    while i <= j:
        while A[i] < pivot: i += 1
        while A[j] > pivot: j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            j, i = j - 1, i + 1
    return i, j

def main():
    count_segments, _ = map(int, input().split())
    starts_of_segments = [0]*count_segments
    ends_of_segments = [0]*count_segments

    for i in range(count_segments):
        left, right = map(int, input().split())
        starts_of_segments[i] = left
        ends_of_segments[i] = right

    points = list(map(int, input().split()))
    quick_sort(starts_of_segments, 0, count_segments-1)
    quick_sort(ends_of_segments, 0, count_segments-1)

    for x in points:
        print(bisect_right(starts_of_segments, x) - bisect_left(ends_of_segments, x), end=' ')

if __name__ == '__main__':
    main()

