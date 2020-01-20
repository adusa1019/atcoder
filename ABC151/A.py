def solve(string):
    return str(chr(ord(string) + 1))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
