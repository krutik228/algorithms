import math





def main():
    def Q2(p, n, r):
        sum_Q = 0
        if r == 1:
            return p_i(p, n + 1, r)
        for i in range(1, r):
            sum_Q += i * (p / n) ** i
        return sum_Q * p_i(p, n, r)

    def Q(p, n, r):
        sum_Q = 0
        if r == 1:
            return p_i(p, n + 1, r)
        for i in range(1, r):
            sum_Q += i * p_i(p, n + i, r)
        return sum_Q

    p_i = lambda p, i, r: ((1 - p) / (1 - p ** (r + 2) + 1e-15)) * p ** i

    Pi = lambda p, n, r: p_i(p, n + r, r)

    Pi2 = lambda p, n, r: (p ** (n + r)) / (math.factorial(n) * n ** r) * P_0(p, n, r)

    n_avg = lambda p, n, r: p * (1 - Pi(p, n, r))

    w_avg = lambda p, n, r: ((n * _nu - (p / n) ** r * ((r + 1) * n * _nu - r * _lam)) / (n * _nu - _lam) ** 2) * (
                (p_i(p, n, r)) / (1 - Pi(p, n, r)))

    w_avg1 = lambda p, n, r: (n * _nu - (p / n) ** r * ((r + 1) * n * _nu - r * _lam)) / (n * _nu - _lam) ** 2 * (
        p_i(p, n, r)) / (1 - Pi(p, n, r))

    w_avg2 = lambda p, n, r: Q2(p, n, r) / ((1 - Pi(p, n, r)) * _lam)

    N2 = lambda p, n, r: Q(p, n, r) + n_avg(p, n, r)

    v = lambda p, n, r: (Q(p, n, r) / _lam) + (1 - Pi(p, n, r)) / _nu

    n_avg2 = lambda p, n, r: N(p, n, r) - Q(p, n, r)

    def P_0(p, n, r):
        summa = 0
        for i in range(0, n - 1):
            summa += (p ** i) / math.factorial(i) + (p ** n) / math.factorial(n)

        for i in range(0, r):
            summa += (p / n) ** i

        return summa ** -1 if summa != 0 else 0

    def N(p, n, r):
        sum = 0
        for i in range(0, n - 1):
            sum += (i * ((p ** i) / math.factorial(i))) + ((p ** n) / math.factorial(n))
        for i in range(0, r):
            sum += (n + i) * ((p / n) ** i)
        return sum * P_0(p, n, r)

    def p_i2(p, n, i):
        sum = 0
        for j in range(0, n):
            sum += (p ** j) / math.factorial(j)
        return sum ** -1 * (p ** i) / math.factorial(i)

    mst = 77
    mtba = 44
    _nu = 1 / mst
    _lam = 1 / mtba
    _r = 3
    _n = 2
    p, n, r = mst/mtba, _n, _r



    print(N(p, n, r), 'N')
    # print(N2(p, n, r), 'N2')
    print(v(p, n, r), 'v')
    print(Q(p, n, r), 'Q')
    # print(Q2(p, n, r), 'Q2')
    # print(Pi(p, n, r), 'Pi')
    # print(n_avg(p, n, r), 'n_avg')
    # print(w_avg2(p, n, r))
    # print(w_avg1(p, n, r))
    # print(w_avg(p, n, r))
    # print(N(p, n, r))
    # print(N2(p, n, r))


def main2():
    R = 3  # Queue
    MTBA = 44  # Create
    MST = 77  # Resource
    __n = 2  # Number of Processes

    p_rounded_id1 = MST/MTBA

    def p0_id2():
        summa = 0
        for i in range(0, __n - 1):
            summa += ((p_rounded_id1 ** i) / math.factorial(i)) + ((p_rounded_id1 ** __n) / math.factorial(__n))
        for i in range(0, R):
            summa += (p_rounded_id1 / __n) ** i
        return summa ** -1 if summa != 0 else 0

    def P0_id7():
        summa = 0
        for i in range(0, __n - 1):
            summa += ((p_rounded_id1 ** i) / math.factorial(i))
        return summa * p0_id2()

    def N_id9():
        summa = 0
        for i in range(0, __n - 1):
            summa += (i * (p_rounded_id1 ** i) / math.factorial(i)) + ((p_rounded_id1 ** __n) / math.factorial(__n))
        for i in range(0, R):
            summa += ((__n + i)*((p_rounded_id1 / __n) ** i))
        return summa * P0_id7()

    print(N_id9())


if __name__ == '__main__':
    main2()
    main()