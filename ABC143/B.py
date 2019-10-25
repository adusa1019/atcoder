def solve(string):
    n, *d = map(int, string.split())
    return str(sum([d1 * d2 for i, d1 in enumerate(d) for d2 in d[i + 1:]]))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
