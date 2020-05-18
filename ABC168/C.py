from math import cos, sin, pi


def c(l, t):
    return l * cos(t), l * sin(t)


def d(a, b, c, d):
    return ((a - c)**2 + (b - d)**2)**0.5


def solve(string):
    a, b, h, m = map(int, string.split())
    return str(d(*c(a, (h + m / 60) / 6 * pi), *c(b, m / 30 * pi)))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
