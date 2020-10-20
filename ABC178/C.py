def solve(string):
    n = int(string)
    m = 10**9 + 7
    return str((pow(10, n, m) + pow(8, n, m) - 2 * pow(9, n, m)) % m)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
