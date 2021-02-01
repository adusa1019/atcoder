def solve(string):
    return str(max(int(string), 0))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
