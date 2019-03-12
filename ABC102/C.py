def solve(string):
    n, *a = map(int, string.split())
    a = sorted([_a - i - 1 for i, _a in enumerate(a)])
    median = a[len(a) // 2]
    return str(sum([abs(_a - median) for _a in a]))


if __name__ == '__main__':
    print(solve("\n".join([input(), input()])))
