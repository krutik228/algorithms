import math
import random


def test(gcd, n_iter=100):
    for i in range(n_iter):
        c = random.randint(0, 1024)
        a = c * random.randint(0, 128)
        b = c * random.randint(0, 128)
        assert gcd(a, a) == gcd(a, 0) == a
        assert gcd(b, b) == gcd(b, 0) == b
        assert gcd(a, 1) == gcd(b, 1) == 1
        d = gcd(a, b)
        assert a % d == b % d == 0


def gcd1(a,b):
    assert a >= 0 and b >= 0
    for d in reversed(range(max(a, b) + 1)):
        if d == 0 or a % d == b % d == 0:
            return d


def gcd2(a, b):
    assert a >=0 and b >=0
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)


def gcd3(a, b):
    assert a >= 0 and b >=0
    if a == 0 or b == 0:
        return max(a, b)
    elif a >= b:
        return gcd3(a % b, b)
    else:
        return gcd3(a, b % a)


def gcd4(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    else:
        return gcd4(b % a, a)


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return gcd(a % b, b)
    if b >= a:
        return gcd(a, b % a)


def main():
    print(gcd(153_653_760_00, 28_892_160))


if __name__ == "__main__":
    main()