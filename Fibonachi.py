import math


def native_fib(n):
    assert n >= 0
    return n if n <= 1 else native_fib(n-1) + native_fib(n-2)


def fib_module(n, m):
    module = fib_iterative(m)
    F = round(((((1 + math.sqrt(5)) / 2) ** n % module) - (((1 - math.sqrt(5)) / 2) ** n) % module)/math.sqrt(5))
    return F


def fib_iterative(n):
    assert n >= 0
    prev, cur = 0, 1
    for i in range(1, n):
        prev, cur = cur, prev + cur
    return cur


def main():
    n = int(input())
    # m = int(input())
    # print(fib_module(n,m))
    print(fib_iterative(n))
    # print(native_fib(35))


if __name__ == "__main__":
    main()