from random import randint
from collections import Counter


def roll_dice(*dice, num_trials=1_000_000):
    """Бросок костей, вероятность выпадения каждого числа """
    counts = Counter()
    for roll in range(num_trials):
        counts[sum((randint(1, side)) for side in dice)] += 1

    print(f"\nOUTCOME PROBABILITY")

    for outcome in sorted(counts):
        print(f"{outcome}\t\t{counts[outcome]/num_trials:0.5f}%")


if __name__ == '__main__':
    roll_dice(6, 6)
