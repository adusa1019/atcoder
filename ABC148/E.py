def solve(string):
    n = int(string)
    if n % 2:
        return "0"
    else:
        ans = 0
        base = 10
        while base <= n:
            ans += n // base
            base *= 5
        return str(ans)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
