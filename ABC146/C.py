def solve(string):
    a, b, x = map(int, string.split())
    l, r = 0, min(x, 10**9) + 1
    while r - l > 1:
        m = (l + r) // 2
        if x < a * m + b * len(str(m)):
            r = m
        else:
            l = m
    return str(l)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
