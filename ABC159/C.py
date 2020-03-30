def solve(string):
    l = int(string)
    return str((l / 3)**3)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
