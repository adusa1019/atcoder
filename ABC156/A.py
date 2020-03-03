def solve(string):
    n, r = map(int, string.split())
    return str(r + max(10 - n, 0) * 100)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
