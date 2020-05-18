def solve(string):
    import numpy
    from itertools import product
    n, m, x, *ca = map(int, string.split())
    ca = numpy.array(ca).reshape((-1, m + 1)).T
    c, a = ca[0], ca[1:]
    ans = n * 10**5 + 1
    for b in product([0, 1], repeat=n):
        b = numpy.array(b)
        if (a @ b.T).min() >= x:
            ans = min(ans, c @ b.T)
    return str(ans if ans <= n * 10**5 else -1)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
