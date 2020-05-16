def solve(string):
    a, b, c, d = map(int, string.split())
    return "No" if (a - 1) // d + 1 < (c - 1) // b + 1 else "Yes"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
