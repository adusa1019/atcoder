from numpy import argmin


def solve(string):
    n, t, a, *h = map(int, string.split())

    return str(argmin([abs(t - _h * 0.006 - a) for _h in h]) + 1)


if __name__ == '__main__':
    print(solve("\n".join([input(), input(), input()])))
