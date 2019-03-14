from itertools import product

import numpy as np


def solve(string):
    n, m, *xyz = map(int, string.split())
    xyz = [[x, y, z] for x, y, z in zip(xyz[::3], xyz[1::3], xyz[2::3])]
    xyz = np.asarray(xyz)
    ans = 0
    for i, j, k in product([-1, 1], repeat=3):
        tmp = xyz.copy()
        tmp[:, 0] = i * xyz[:, 0]
        tmp[:, 1] = j * xyz[:, 1]
        tmp[:, 2] = k * xyz[:, 2]
        base = sum(sorted(np.sum(tmp, axis=1), reverse=True)[:m])
        ans = max(ans, base)
    return str(ans)


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve('{} {}\n'.format(n, m) + '\n'.join([input() for _ in range(n)])))
