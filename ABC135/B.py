def solve(string):
    n, *p = map(int, string.split())
    return "NO" if sum([i != _p for i, _p in enumerate(p, start=1)]) > 2 else "YES"


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
