def solve(string):
    n, *a = map(int, string.split())
    a = sorted(a, reverse=True)
    return str(sum(a[::2]) - sum(a[1::2]))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
