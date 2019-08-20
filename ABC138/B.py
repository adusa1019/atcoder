def solve(string):
    n, *a = map(int, string.split())
    return str(1 / sum(1 / _a for _a in a))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
