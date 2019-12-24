def solve(string):
    n, *a = map(int, string.split())
    c = 1
    for _a in a:
        if c == _a:
            c += 1
    return str(-1 if c == 1 else n - c + 1)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
