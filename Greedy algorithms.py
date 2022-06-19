
def greedy_me():
    a = []
    n = int(input())
    for i in range(n):
        a.append(input().split())
    a = [list(map(int, i)) for i in a]
    a.sort(key=lambda x: x[1])

    b = []
    cur = a[0][1]
    b.append(cur)
    for i in a[1:]:
        if i[0] <= cur:
            continue
        else:
            cur = i[1]
            b.append(cur)

    print(len(b))
    print(' '.join(map(str, b)))


def greedy1():
    segments = sorted([sorted(map(int, input().split())) for i in range(int(input()))], key=lambda x: x[1])
    print(segments)
    dots = [segments.pop(0)[1]]
    print(segments.pop(0))
    print(dots)
    for l, r in segments:
        if l > dots[-1]:
            dots.append(r)
    print(str(len(dots)) + '\n' + ' '.join(map(str, dots)))


def greedy_me1():
    n = int(input())
    segments = [list(map(int, input().split())) for _ in range(n)]
    segments = sorted(segments, key=lambda x: x[1])

    # print(segments)

    points = [segments.pop(0)[1]]
    for l, r in segments:
        if l > points[-1]:
            points.append(r)

    print(len(points))
    print(*points)


if __name__ == '__main__':
    greedy_me1()
    # greedy1()
