import numpy as np


def solve(string):
    n, *a = map(int, string.split())
    a = ("{:060b}".format(_a) for _a in a)
    m, ans = 10**9 + 7, 0
    for s in map(lambda x: x.count("1"), zip(*a)):
        ans <<= 1
        ans += s * (n - s)
        ans %= m
    return str(ans)


def np_solve(string):
    n, *a = map(int, string.split())
    a = np.asarray(a)
    m, ans = 10**9 + 7, 0
    for i in range(60):
        s = int((a & 1).sum())
        a >>= 1
        ans += s * (n - s) * pow(2, i, m) % m
        ans %= m
    return str(ans)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
