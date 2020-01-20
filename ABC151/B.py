def solve(string):
    n, k, m, *a = map(int, string.split())
    t = n * m - sum(a)
    return str(max(t, 0)) if t <= k else "-1"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
