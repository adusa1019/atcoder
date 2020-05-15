def solve(string):
    n, k = map(int, string.split())
    n %= k
    return str(min(n, abs(n - k)))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
