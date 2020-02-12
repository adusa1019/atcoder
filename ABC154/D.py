from itertools import accumulate


def solve(string):
    n, k, *p = map(int, string.split())
    *p, = accumulate((1 + _p) / 2 for _p in p)
    return str(max(p2 - p1 for p1, p2 in zip(p, p[k:]))) if k < n else str(p[-1])


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
