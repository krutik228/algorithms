


def main():
    # n = int(input())
    # A = list(map(int, input().split()))
    # n = 10
    A = [3, 6, 12, 7, 9, 24, 18, 3, 9, 24]
    n = len(A)
    D = [1]*n
    for i in range(n):
        D[i] = 1
        for j in range(0, i):
            if (A[i] % A[j] == 0) and (D[j] + 1 > D[i]):
                D[i] = max(D[j] + 1, D[i])


if __name__ == '__main__':
    main()