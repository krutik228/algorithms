import collections
from heapq import heappush, heappop
from collections import Counter


def Hoffman2():
    prefix = lambda a, p: [(k, p + v) for k, v in a]
    print(prefix, '-prefix')
    merge = lambda a, b: (a[0] + b[0], prefix(a[1], '0') + prefix(b[1], '1'))
    print(merge, '-merge')

    string = input()
    heap = [(v, [(k, '')]) for k, v in reversed(Counter(string).most_common())]

    while len(heap) > 1:
        heappush(heap, merge(heappop(heap), heappop(heap)))

    table = heap[0][1] if len(heap[0][1]) > 1 else prefix(heap[0][1], '0')
    encoded = string.translate(str.maketrans(dict(table)))

    print(len(table), len(encoded))
    print(*map('{0[0]}: {0[1]}'.format, table), encoded, sep='\n')

def Hoffman1():

    def popmin(tree, codes, num):
        el = tree.pop(tree.index(min(tree)))
        for s in el[1]:
            codes[s] = num + codes[s]
        return el[0], el[1]

    sss = input().strip()
    count = collections.Counter(sss)
    codes = dict.fromkeys(count, '0' if len(count) == 1 else '')
    print(codes, '- codes')

    tree = [[count[key], key] for key in count]
    while len(tree) > 1:
        val1, s1 = popmin(tree, codes, '0')  # 1, '!'
        val2, s2 = popmin(tree, codes, '1')  # 1, 'r'
        tree.append([val1 + val2, s1 + s2])  # 2, '!r'
    print(tree, '- tree2')
    word = ''.join(codes[s] for s in sss)
    print(len(count), len(word))
    [print('{}: {}'.format(k, codes[k])) for k in sorted(codes)]
    print(word)

def Hoffman_me1():

    def popmin(tree, codes, num):
        print(tree, codes, num, '- popmin')
        el = tree.pop(tree.index(min(tree)))
        print(el, '- el')
        for s in el[1]:
            codes[s] = num + codes[s]
        return el[0], el[1]

    string = input()

    count = Counter(string)

    tree = [[count[key], key] for key in count]


    codes = dict.fromkeys(count, '0' if len(count) == 1 else '')

    while len(tree) > 1:
        freq, symb = popmin(tree, codes, '0')
        freq1, symb1 = popmin(tree, codes, '1')
        tree.append([freq + freq1, symb + symb1])



    res = ''.join(codes[s] for s in string)

    print(len(set(string)), len(res))
    [print(f'{codes[k]}: {k}') for k in sorted(codes)]
    print(res)


def Hoffman_me():
    string = input()
    if len(string) == 1:
        print(1, 1)
        print(f'{string}: 0')
        print(0)
        return

    if len(set(string)) == 1:
        print(1, len(string))
        print(f'{string[0]}: 0')
        print(len(string) * '0')
        return

    freq = {}
    for i in string:
        freq[i] = freq.get(i, 0) + 1
    tuples = sorted(freq.items(), key=lambda item: item[1])

    # print(tuples)

    code_freq = []

    while len(tuples) != 1:
        tuples = (sorted([k for k in tuples], key=lambda k: (k[1], k[0])))
        code_freq.append(((tuples[0][0], tuples[0][1]), 0))
        tuples[0] = (tuples[0][0] + tuples[1][0], tuples[0][1] + tuples[1][1])
        code_freq.append(((tuples[1][0], tuples[1][1]), 1))
        tuples.pop(1)

    codes = []
    for k_f, cd in code_freq:
        tmp = ''
        for key_freq, code in code_freq:
            if k_f[0] in key_freq[0]:
                tmp += str(code)
        codes.append((k_f[0], tmp[::-1]))
    # print(codes)

    res = ''
    for let in string:
        for key_code in codes:
            if let == key_code[0]:
                res += key_code[1]
    # print(res)

    new_codes = []

    for i in codes:
        if len(i[0]) == 1:
            new_codes.append(i)

    new_codes = sorted(new_codes, key=lambda x: x[0])
    print(len(set(string)), len(res))
    [print(f'{k}: {v}') for k, v in new_codes]
    print(res)


def main():
    # Hoffman_me1()
    # Hoffman1()
    Hoffman2()
if __name__ == '__main__':
    main()
