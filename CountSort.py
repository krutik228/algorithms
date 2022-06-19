
def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = [0] * 11
    for j in range(n):
        B[A[j]] += 1
    for i in range(1, 11):
        B[i] += B[i-1]
        
    A_new = [0] * n

    for j in range(n-1, -1, -1):
        A_new[B[A[j]] - 1] = A[j]
        B[A[j]] -= 1

    print(*A_new)


if __name__ == '__main__':
    main()
