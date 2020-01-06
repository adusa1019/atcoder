def solve(string):
    return "".join(string.split()[::-1])


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
