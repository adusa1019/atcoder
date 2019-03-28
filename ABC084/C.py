from math import ceil


def solve(string):
    n, *csf = map(int, string.split())
    f_list = []
    for c, s, f in zip(csf[::3], csf[1::3], csf[2::3]):
        f_list = [c + ceil((max(_f, s)) / f) * f for _f in f_list]
        f_list.append(c + s)
    f_list.append(0)
    return "\n".join([str(_f) for _f in f_list])


if __name__ == '__main__':
    n = int(input())
    print(solve('{}\n'.format(n) + '\n'.join([input() for _ in range(n - 1)])))
