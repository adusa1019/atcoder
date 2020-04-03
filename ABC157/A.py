def solve(string):
    return str((int(string) + 1) // 2)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
