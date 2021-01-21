def _solve(string):
    x, y, a, b = map(int, string.split())
    ans = 0
    while a * x < b and a * x < y:
        x *= a
        ans += 1
    ans += (y - x - 1) // b
    return str(ans)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
