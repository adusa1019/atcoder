def solve(string):
    w, h, x, y = map(int, string.split())
    f = 1 if 2 * x == w and 2 * y == h else 0
    return str("{} {}".format(w * h / 2, f))


if __name__ == '__main__':
    print(solve(input()))
