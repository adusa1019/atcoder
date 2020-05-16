def solve(string):
    a, b, n = map(int, string.split())
    return str(a * n // b) if b > n else str(a * (b - 1) // b)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
