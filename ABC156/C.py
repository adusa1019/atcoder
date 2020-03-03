def solve(string):
    n, *x = map(int, string.split())
    return str(sum((_x - int(sum(x) / n + 0.5))**2 for _x in x))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
