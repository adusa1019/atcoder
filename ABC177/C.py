from itertools import accumulate


def solve(string):
    _, *a = map(int, string.split())
    ac = list(accumulate(a))
    ans = 0
    for _a, _c in zip(a, ac):
        ans = (ans + _a * (ac[-1] - _c)) % (10**9 + 7)
    return str(ans)


def short_solve(string):
    _, *a = map(int, string.split())
    return str((sum(a)**2 - sum(map(lambda x: x**2, a))) // 2 % (10**9 + 7))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
