def fib_list(n, m):
    a = [0, 1]
    for i in range(2, m*6):
        a.append((a[i-1] + a[i-2]) % m)
        if a[-1] == 1 and a[-2] == 0:
            return a[n % (len(a)-2)]

if __name__ == "__main__":
    n, m = map(int, input().split())
    fib_list(n, m)

