def solve(string):
    a, b, c, d = map(int, string.split())
    return str(max(a * c, a * d, b * c, b * d))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
