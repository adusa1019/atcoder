from itertools import product


def solve(string):
    n, *xy = map(int, string.split())
    *xy, = zip(*[iter(xy)] * 2)
    return str(
        sum(((xy[i][0] - xy[j][0])**2 + (xy[i][1] - xy[j][1])**2)**0.5
            for i, j in product(range(n), repeat=2)) / n)


if __name__ == '__main__':
    n = int(input())
    print(solve('{}\n'.format(n) + '\n'.join([input() for _ in range(n)])))
