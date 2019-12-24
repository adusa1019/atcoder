def solve(string):
    n, s, t = string.split()
    return "".join(_s + _t for _s, _t, in zip(s, t))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
