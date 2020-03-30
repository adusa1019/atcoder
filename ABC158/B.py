def solve(string):
    n, a, b = map(int, string.split())
    return str(n // (a + b) * a + min(n % (a + b), a))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
