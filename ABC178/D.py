def solve(string):
    from scipy.special import comb
    s = int(string)
    ans, m = 0, 10**9 + 7
    for i in range(1, s // 3 + 1):
        ans += comb(s - 2 * i - 1, i - 1, exact=True) % m
    return str(ans % m)


def fast_solve(string):
    s = int(string)
    m = 10**9 + 7
    a = [0] * (s + 1)
    if s <= 2:
        return "0"
    if s <= 5:
        return "1"
    a[0] = a[1] = a[2] = 0
    a[3] = a[4] = a[5] = 1
    for i in range(6, s + 1):
        a[i] = (a[i - 1] + a[i - 3]) % m
    return str(a[-1] % m)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
