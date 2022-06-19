def quick_sort_best1():

    from bisect import bisect_left, bisect_right

    n, m = map(int, input().split())
    a, b = map(sorted, zip(*(map(int, input().split()) for _ in range(n))))
    print(*(bisect_right(a, p) - bisect_left(b, p) for p in map(int, input().split())))


def quick_sort_best2():
    return


if __name__ == '__main__':
    quick_sort_best1()
