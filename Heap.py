from heapq import *


def main():
    out = []
    heap = []
    heapify(heap)
    count = 0
    k = int(input())
    for i in range(k):
        command = input().split()
        if command[0] == 'Insert':
            # heap.append(int(command[1]) * -1)
            heappush(heap, int(command[1]) * -1)
        if command[0] == 'ExtractMax':
            m = heappop(heap)
            out.append(m)

    [print(i) for i in out]

if __name__ == '__main__':
    main()
