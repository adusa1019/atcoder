from itertools import accumulate


def solve(string):
    n, *a = map(int, string.split())
    *a, = accumulate(a)
    *aa, = accumulate(a)
    ms, c = [], 0
    for _a in a:
        if _a > c:
            c = _a
        ms.append(c)
    return str(max(0, *[_a + _s for _a, _s in zip([0] + aa[:-1], ms)], aa[-1]))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
