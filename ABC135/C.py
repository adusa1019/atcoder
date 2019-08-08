def solve(string):
    n, *ab = map(int, string.split())
    a, b = ab[:n + 1], ab[n + 1:]
    _sum = sum(a)
    for i, _b in enumerate(b[::-1]):
        diff = min(a[n - i], _b)
        _b -= diff
        a[n - i] -= diff
        a[n - i - 1] = max(0, a[n - i - 1] - _b)
    return str(_sum - sum(a))


if __name__ == '__main__':
    n = int(input())
    print(solve('{}\n'.format(n) + '\n'.join([input() for _ in range(2)])))
