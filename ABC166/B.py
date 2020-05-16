def solve(string):
    n, k, *da = map(int, string.split())
    t, i = [True] * n, 0
    for _ in range(k):
        d = da[i]
        for j in da[i + 1:i + 1 + d]:
            t[j - 1] = False
        i += d + 1
    return str(sum(t))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
