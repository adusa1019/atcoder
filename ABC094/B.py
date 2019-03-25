def solve(string):
    n, m, x, *a = map(int, string.split())
    lows = sum([_a < x for _a in a])
    return str(min(lows, m - lows))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
