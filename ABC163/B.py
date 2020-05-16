def solve(string):
    n, m, *a = map(int, string.split())
    return str(b if (b := n-sum(a)) >= 0 else -1)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
