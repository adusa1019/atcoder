def solve(string):
    a, b, c, k = map(int, string.split())
    if k <= a:
        return str(k)
    if k <= a + b:
        return str(a)
    return str(2 * a + b - k)
    pass


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
