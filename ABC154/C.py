def solve(string):
    n, *a = map(int, string.split())
    return "YES" if len(a) == len(set(a)) else "NO"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
