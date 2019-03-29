import numpy as np


def solve(string):
    n, m, c, *ba = map(int, string.split())
    b = np.asarray(ba[:m])
    a = np.asarray(ba[m:])
    a.resize((n, m))
    return str(np.sum(np.dot(a, b.T) > -c))


if __name__ == '__main__':
    n, m, o = map(int, input().split())
    print(solve('{} {} {}\n'.format(n, m, o) + '\n'.join([input() for _ in range(n + 1)])))
