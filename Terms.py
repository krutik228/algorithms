
def main():
    """Наиболее длинна последовательность. На вход подаётся число, результатом будет
    возрастающая последовательность чисел, которые в сумме дают переданное число,
    а также длина этой последовательности"""
    digits = []
    num = int(input())
    summa = 0
    if num in (1, 2):
        return [num]
    for i in range(1, num):
        if summa == num:
            break
        elif summa + i > num:
            digits[-1] += num - summa
            break
        else:
            digits.append(i)
            summa += i
    return digits

if __name__ == '__main__':
     res = main()
     print(len(res))
     print(*res)
