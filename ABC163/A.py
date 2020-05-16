def solve(string):
    from math import pi
    return str(2 * int(string) * pi)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
