def solve(string):
    n, *d = map(int, string.split())
    d = sorted(d)
    return str(d[n//2]-d[n//2-1])


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
