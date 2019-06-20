from itertools import accumulate


def solve(string):
    n, *w = map(int, string.split())
    *w, = accumulate(w)
    return str(min([abs(w[-1] - 2 * w[i]) for i in range(n - 1)]))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
