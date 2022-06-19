
def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg



    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos > 0


    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
    # iterable - исходная последовательность
    # funcs - допускающие функции
    # judge - решающая функция
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge


    def __iter__(self):
        for x in self.iterable:
            pos, neg = 0, 0
            for fun in self.funcs:
                if fun(x):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield x


a = [i for i in range(31)]
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))