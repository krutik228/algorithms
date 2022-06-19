import random

Q = [
    0.3015,
    0.3863,
    0.4414,
    0.496,
    0.54,
]

# [print(round(i - i * random.randint(0, 10) / 100, 3)) for i in Q]

N1retry = [
    0.933,
    0.410,
    0.234,
    0.111,
    0.03,
]
N2retry = [
    1.251,
    0.559,
    0.350,
    0.168,
    0.038,
]
nu = 132
y = 205

for i in range(len(N1retry)):
    # print(nu + y * N1retry[i])
    print(y * N2retry[i])
