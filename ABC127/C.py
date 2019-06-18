from itertools import accumulate
from collections import Counter


def solve(string):
    n, m, *lr = map(int, string.split())
    t = [0] * (n + 2)
    for l, r in zip(*[iter(lr)] * 2):
        t[l] += 1
        t[r + 1] -= 1
    *t, = accumulate(t)
    c = Counter(t)
    return str(c[m]) if m in c.keys() else "0"


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve('{} {}\n'.format(n, m) + '\n'.join([input() for _ in range(m)])))
