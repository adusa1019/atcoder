from fractions import gcd
from functools import reduce


def lcm(a, b):
    return a * b // gcd(a, b)


def solve(string):
    n, m, *a = map(int, string.split())
    c = 2**len(bin(a[0]).split("1")[-1])
    l = reduce(lcm, (_a if not _a % c and _a // c % 2 else 2 * m + 2 for _a in a))
    return str((m - l // 2) // l + 1) if l <= 2 * m else "0"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
