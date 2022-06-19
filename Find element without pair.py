"""Найти элемент без пары"""


def find_element_without_pair3(l):
    xor_sum = 0
    for i in l:
        xor_sum ^= i
    return xor_sum


def find_element_without_pair2(x):
    d = {}
    for i in x:
        d.update({i: d.get(i, 0)+1})
        if d.get(i) == 2:
            d.pop(i)
    return list(d.items())[0][0]


def find_element_without_pair(sequence):
    summa = sum(sequence)
    summa_unique = sum(set(sequence))
    return summa_unique * 2 - summa


if __name__ == '__main__':
    print(find_element_without_pair([2, 3, 2, 1, 3, 9, 1]))
    print(find_element_without_pair2([2, 3, 2, 1, 3, 9, 1]))
    print(find_element_without_pair3([2, 3, 2, 1, 3, 9, 1]))
