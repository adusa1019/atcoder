def solve(string):
    n, k, *x = map(int, string.split())
    x = sorted(x)
    diff = [
        _x1 - _x0 + min(abs(_x0), abs(_x1)) if _x0 <= 0 <= _x1 else max(abs(_x0), abs(_x1))
        for _x0, _x1 in zip(x, x[k - 1:])
    ]
    return str(min(diff))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
