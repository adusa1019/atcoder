def solve(string):
    a, b = map(int, string.split())
    return str(2 * a + 100 - b)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
