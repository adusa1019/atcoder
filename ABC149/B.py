def solve(string):
    a, b, k = map(int, string.split())
    return "{} {}".format(max(0, a - k), max(0, min(b, a + b - k)))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
