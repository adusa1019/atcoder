def mulmod(x, y, p=10**9 + 7):
    return x * y % p


def combmod(n, k, p=10**9 + 7):
    from functools import reduce
    k = min(k, n - k)
    x = reduce(mulmod, range(n - k + 1, n + 1), 1)
    y = reduce(mulmod, range(1, k + 1), 1)
    return x * pow(y, p - 2, p) % p


def solve(string):
    n, a, b = map(int, string.split())
    return str((pow(2, n, 10**9 + 7) - 1 - combmod(n, a) - combmod(n, b)) % (10**9 + 7))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
