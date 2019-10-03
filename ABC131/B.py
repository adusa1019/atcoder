def solve(string):
    n, l = map(int, string.split())
    _sum = l * n + n * (n - 1) // 2
    if l >= 0:
        _sum -= l
    elif l + n - 1 < 0:
        _sum -= l + n - 1
    return str(_sum)


if __name__ == '__main__':
    print(solve(input()))
