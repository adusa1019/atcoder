from math import gcd
from itertools import product


def solve(string):
    k = int(string)
    ans = 0
    for a, b, c in product(range(1, k + 1), repeat=3):
        ans += gcd(gcd(a, b), c)
    return str(ans)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
