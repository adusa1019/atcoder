from collections import Counter
from itertools import accumulate


def solve(string):
    n, m, *a = map(int, string.split())
    d = Counter(_a % m for _a in accumulate([0] + a))
    return str(sum(v * (v - 1) // 2 for v in d.values()))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
