from collections import Counter


def find_uniq(strings: list) -> str:
    i = 0
    res = [list(set(i.lower())) for i in strings]
    while res.count(res[i]) != 1:
        i += 1
    return strings[i]

    # for i in range(1, len(strings) - 1):
    #     prev = set(strings[i-1].lower())
    #     cur = set(strings[i].lower())
    #     fut = set(strings[i+1].lower())
    #     if not prev == cur == fut:
    #         if (prev != cur) and (prev != fut):
    #             return strings[i-1]
    #         if (prev != cur) and (cur != fut):
    #             return strings[i]
    #         else:
    #             return strings[i+1]


if __name__ == '__main__':
    print(find_uniq(['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba']))
    print(find_uniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']))
    print(find_uniq(['abc', 'acb', 'bac', 'bcca', 'bca', 'cab', 'cba', 'bfa']))
    print(find_uniq(['abc', 'acb', 'bac', 'bcca', 'bca', 'cab', 'cba']))

