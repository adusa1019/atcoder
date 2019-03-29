def solve(string):
    h, w, _h, _w = map(int, string.split())
    return str((h - _h) * (w - _w))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
