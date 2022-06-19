import time
from matplotlib import pyplot as plt


def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1-t0)
    return acc


def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n-1)


def fib2(n):
    assert n >= 0
    pre, cur = 0, 1
    for i in range(1, n):
        pre, cur = cur, pre + cur
    return cur


def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
        plt.legend()
        plt.grid(True)
    plt.show()


if __name__ == '__main__':
    # print(timed(fib1, 20))
    compare([fib1, fib2], list(range(800)))
