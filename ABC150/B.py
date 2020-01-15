def solve(string):
    n, s = string.split()
    return str(len(s.split("ABC")) - 1)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
