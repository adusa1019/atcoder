def solve(string):
    _, *a = map(int, string.split())
    ans = step = 0
    for a0, a1 in zip(a, a[1:]):
        step = max(0, a0 + step - a1)
        ans += step
    return str(ans)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
