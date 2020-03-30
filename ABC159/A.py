def solve(string):
    n, m = map(int, string.split())
    return str((n + m) * (n + m - 1) // 2 - n * m)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
