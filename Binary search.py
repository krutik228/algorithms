import math

def binary_find(x, array):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = int((left + right)/2)
        if array[middle] == x:
            return middle + 1
        elif array[middle] > x:
            right = middle - 1
        else:
            left = middle + 1
    return -1

def main():
    n, *A = map(int, input().split())
    k, *B = map(int, input().split())
    [print(binary_find(x, A), end=' ') for x in B]

if __name__ == '__main__':
    main()