from itertools import product


def solve(string):
    n = int(string)
    t = [[0] * 10 for _ in range(10)]
    for i in range(n + 1):
        i = str(i)
        t[int(i[0])][int(i[-1])] += 1
    return str(sum(t[i][j] * t[j][i] for i, j in product(range(1, 10), repeat=2)))


def faster_solve(string):
    d = len(string)
    if d == 1:
        return string
    s0, ss, sn = int(string[0]), int(string[1:-1] or 0), int(string[-1])
    t = [[0] * 10] + [[int("1" * (d - 2) or 0)] * 10 for _ in range(9)]
    for i in range(1, 10):
        t[i][i] += 1
    for i, j in product(range(1, s0), range(10)):
        t[i][j] += 10**(d - 2)
    for j in range(10):
        t[s0][j] += ss + 1 if j <= sn else ss
    return str(sum(t[i][j] * t[j][i] for i, j in product(range(1, 10), repeat=2)))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
