import numpy as np


def solve(string):

    n, m, *py = map(int, string.split())
    py = [(_p, _y) for _p, _y in zip(py[0::2], py[1::2])]
    p = [[] for _ in range(n)]
    for _p, _y in py:
        p[_p - 1].append(_y)
    for i in range(n):
        p[i] = np.argsort(np.argsort(p[i]))

    counter = [0 for _ in range(n)]
    ans = []
    for _p, _y in py:
        ans.append("{:06}{:06}".format(_p, p[_p - 1][counter[_p - 1]] + 1))
        counter[_p - 1] += 1
    return "\n".join(ans)


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve("{} {}\n".format(n, m) + "\n".join([input() for _ in range(m)])))
