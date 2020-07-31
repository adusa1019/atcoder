def solve(string):
    return "A" if ord(string) < ord('a') else "a"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
