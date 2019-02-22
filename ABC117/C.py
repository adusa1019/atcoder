import numpy as np


def solve(string):
    n, m, *x = map(int, string.split())
    x = sorted(np.diff(sorted(x)), reverse=True)
    return str(sum(x[n - 1:]))


if __name__ == '__main__':
    print(solve("\n".join([input(), input()])))
