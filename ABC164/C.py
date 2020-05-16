def solve(string):
    return str(len(set(string.split())) - 1)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
