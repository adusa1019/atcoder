def solve(string):
    x = int(string)
    return str(x // 500 * 1000 + x % 500 // 5 * 5)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
