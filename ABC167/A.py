def solve(string):
    s, t = string.split()
    return "Yes" if s == t[:-1] else "No"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
