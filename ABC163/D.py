def solve(string):
    from itertools import accumulate
    n, k = map(int, string.split())
    *a, = accumulate(range(n + 1))
    ans, m = 0, 10**9 + 7
    for b, c in zip(a[:-k][::-1], a[k - 1:]):
        ans = (ans + a[-1] - b - c + 1) % m
    return str((ans + 1) % m)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
