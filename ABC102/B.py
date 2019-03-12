def solve(string):
    n, *a = map(int, string.split())
    a = sorted(a)
    return str(abs(a[0] - a[-1]))


if __name__ == '__main__':
    print(solve("\n".join([input(), input()])))
