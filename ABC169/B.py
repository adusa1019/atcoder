def solve(string):
    n, *a = map(int, string.split())
    a = sorted(a)
    if a[0] == 0:
        return "0"
    ans = 1
    for _a in a[::-1]:
        ans *= _a
        if ans > 10**18:
            return "-1"
    return str(ans)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
