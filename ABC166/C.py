def solve(string):
    n, m, *hab = map(int, string.split())
    h, ab = hab[:n], hab[n:]
    t = [True] * n
    for _a, _b in zip(*[iter(ab)] * 2):
        if h[_a - 1] <= h[_b - 1]:
            t[_a - 1] = False
        if h[_a - 1] >= h[_b - 1]:
            t[_b - 1] = False
    return str(sum(t))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
