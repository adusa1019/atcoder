def solve(string):
    n, *p = map(int, string.split())
    ans = 0
    m = n + 1
    for _p in p:
        if _p < m:
            ans += 1
            m = _p
    return str(ans)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
