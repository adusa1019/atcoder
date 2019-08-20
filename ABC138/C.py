def solve(string):
    n, *v = map(int, string.split())
    v = sorted(v, reverse=True)
    return str(sum(_v / 2**i for i, _v in enumerate(v[:-1], start=1)) + v[-1] / 2**(n - 1))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
