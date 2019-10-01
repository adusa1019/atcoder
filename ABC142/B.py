def solve(string):
    n, k, *h = map(int, string.split())
    return str(len([_h for _h in h if _h >= k]))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
