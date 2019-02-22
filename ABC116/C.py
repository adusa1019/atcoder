def solve(string):
    n, *h = map(int, string.split())
    count = 0
    current = 0
    for _h in h:
        count += max(0, _h - current)
        current = _h
    return str(count)


if __name__ == '__main__':
    print(solve("\n".join([input(), input()])))
