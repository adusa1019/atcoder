def solve(string):
    n, *p = map(int, string.split())
    ans = 0
    for i, j, k in zip(p, p[1:], p[2:]):
        ans += 1 if i <= j <= k or i >= j >= k else 0
    return str(ans)


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
