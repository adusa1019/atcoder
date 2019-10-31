from math import atan2, degrees


def solve(string):
    a, b, x = map(int, string.split())
    if x >= a**2 * b / 2:
        c, d = 2 * (a**2 * b - x), a**3
    else:
        c, d = a * b**2, 2 * x
    return str(degrees(atan2(c, d)))


if __name__ == '__main__':
    print(solve(input()))
