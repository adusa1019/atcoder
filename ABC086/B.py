from math import sqrt, floor


def solve(string):
    ab = "".join(string.split())
    r = sqrt(int(ab))
    return "Yes" if r == floor(r) else "No"


if __name__ == '__main__':
    print(solve(input()))
