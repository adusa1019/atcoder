def solve(string):
    return "x" * len(string)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
