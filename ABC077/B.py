from math import floor, sqrt


def solve(string):
    return str(floor(sqrt(int(string)))**2)


if __name__ == '__main__':
    print(solve(input()))
