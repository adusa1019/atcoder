from math import ceil


def solve(string):
    a, b = map(int, string.split())
    return str(ceil((a + b) / 2))


if __name__ == '__main__':
    print(solve(input()))
