def solve(string):
    n, *a = map(int, string.split())
    count = 0
    for _a in a:
        tmp = _a
        while tmp % 2 == 0:
            tmp /= 2
            count += 1
    return str(count)


if __name__ == '__main__':
    print(solve("\n".join([input(), input()])))
