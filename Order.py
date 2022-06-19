import re


def order(sentence):
    """
    There are numbers in the words of the sentence, it is necessary to arrange the words in
    accordance with these numbers. For instance, the first will be the word in which there is a
    number 1, the second 2, etc.

    """
    splited = sentence.split()
    res = [0] * len(splited)
    pattern = r"\d+"
    for i in splited:
        math = re.search(pattern, i)
        res[int(math.group()) - 1] = i
    return ' '.join(res)


def order_by_sort(words):
    """
    There are numbers in the words of the sentence, it is necessary to arrange the words in
    accordance with these numbers. For instance, the first will be the word in which there is a
    number 1, the second 2, etc.

    The maximum number is 9.

    """
    return ' '.join(sorted(words.split(), key=lambda x: sorted(x)))


def order_by_sort_with_re(words):
    """
    There are numbers in the words of the sentence, it is necessary to arrange the words in
    accordance with these numbers. For instance, the first will be the word in which there is a
    number 1, the second 2, etc.

    """
    pattern = r"\d+"
    return ' '.join(sorted(words.split(), key=lambda x: int(re.search(pattern, x).group())))


if __name__ == '__main__':
    text = "4of Fo1r pe6ople g3ood th5e the2 11sad s7dqw d8qwe 12qweqes qwesadad9 xcvx10"
    print(order(text))
    print(order_by_sort(text))
    print(order_by_sort_with_re(text))
