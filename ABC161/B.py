def solve(string):
    n, m, *a = map(int, string.split())
    return "No" if len([_a for _a in a if _a >= sum(a) / 4 / m]) < m else "Yes"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
