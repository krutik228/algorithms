from math import sqrt

"""Разбиение числа на простые множители"""


def find_prime_factors(number):
    divider, factors = 2, []
    while number != 1:
        if number % divider == 0:
            factors.append(divider)
            number = int(number / divider)
        else:
            divider += 1
    return factors


def find_prime_factors_fast(number):
    factors, divider = [], 2

    while divider <= int(sqrt(number)):
        if number % divider == 0:
            factors.append(divider)
            number /= divider
        else:
            divider += 1
    if number > 1:
        factors.append(int(number))
    return factors


if __name__ == '__main__':
    print(find_prime_factors_fast(3543453436363331))
    print(find_prime_factors(3543453436363331))

