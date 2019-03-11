def solve(string):
    n, *a = map(int, string.split())
    return str(sum(a) - n)


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
