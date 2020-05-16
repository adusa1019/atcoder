def f(a, b, c):
    from itertools import product
    return sum(i + j in a for i, j in product(b, c))


def solve(string):
    n, s = string.lower().split()
    r, g, b, r2, g2, b2 = [], [], [], set([]), set([]), set([])
    for i, _s in enumerate(s):
        eval(f"{_s}.append(i)")
        eval(f"{_s}2.add(2 * i)")
    return str(len(r) * len(g) * len(b) - f(r2, g, b) - f(g2, b, r) - f(b2, r, g))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
