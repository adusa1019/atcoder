def solve(string):
    return str(6 - sum(map(int, string.split())))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
