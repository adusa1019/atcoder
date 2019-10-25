def solve(string):
    n, s = string.split()
    return str(int(n) - sum([1 for d1, d2 in zip(s, s[1:]) if d1 == d2]))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
