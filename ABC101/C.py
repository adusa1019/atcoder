from math import ceil


def solve(string):
    n, k, *a = map(int, string.split())
    return str(ceil((n - 1) / (k - 1)))


if __name__ == '__main__':
    print(solve("\n".join([input(), input()])))
