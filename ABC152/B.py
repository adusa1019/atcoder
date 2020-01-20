def solve(string):
    a, b = map(int, string.split())
    return str(a) * b if a < b else str(b) * a


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
