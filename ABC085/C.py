def solve(string):
    n, y = map(int, string.split())
    currents = [10000, 5000, 1000]
    for i in range(0, n + 1):
        _y = y - i * currents[0]
        for j in range(0, n + 1 - i):
            __y = _y - j * currents[1]
            if currents[2] * (n - i - j) == __y:
                return "{} {} {}".format(i, j, n - i - j)
    return "-1 -1 -1"


if __name__ == '__main__':
    print(solve(input()))
