from itertools import accumulate


def solve(string):
    n, x, *l = map(int, string.split())
    return str(len(list(filter(lambda a: a <= x, list(accumulate(l))))) + 1)


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
