def main():
    n, cur_w = map(int, input().split())
    objects = [list(map(int, input().split())) for _ in range(n)]
    objects = list(sorted(objects, key=lambda x: x[0] / x[1], reverse=True))

    total = 0
    for price, weight in objects:
        if cur_w >= weight:
            cur_w -= weight
            total += price
        else:
            total += (cur_w/weight) * price
            break

    print('{:.3f}'.format(total))


if __name__ == '__main__':
    main()
