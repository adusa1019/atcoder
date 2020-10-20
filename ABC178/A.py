def solve(string):
    return str(int(not int(string)))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
