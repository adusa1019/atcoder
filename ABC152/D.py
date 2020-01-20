from itertools import product


def solve(string):
    n = int(string)
    t = [[0] * 10 for _ in range(10)]
    for i in range(n + 1):
        i = str(i)
        t[int(i[0])][int(i[-1])] += 1
    return str(sum(t[i][j] * t[j][i] for i, j in product(range(1, 10), repeat=2)))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
