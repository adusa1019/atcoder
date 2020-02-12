def solve(string):
    s, t, a, b, u = string.split()
    return "{} {}".format(int(a) - (s == u), int(b) - (t == u))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
