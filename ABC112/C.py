from itertools import product


def solve(string):
    n, *xyh = map(int, string.split())
    xyh = sorted([(x, y, h) for x, y, h in zip(xyh[::3], xyh[1::3], xyh[2::3])],
                 key=lambda x: x[-1], reverse=True)
    for i, j in product(range(101), range(101)):
        h = abs(xyh[0][0] - i) + abs(xyh[0][1] - j) + xyh[0][2]
        check = [_h == max(h - abs(_x - i) - abs(_y - j), 0) for _x, _y, _h in xyh[1:]]
        if all(check):
            return "{} {} {}".format(i, j, h)


if __name__ == '__main__':
    n = int(input())
    print(solve("{}\n".format(n) + '\n'.join([input() for _ in range(n)])))
