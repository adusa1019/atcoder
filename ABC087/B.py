def solve(string):
    a, b, c, x = map(int, string.split())
    ans = 0
    for i in range(a + 1):
        for j in range(b + 1):
            if 0 <= x - 500 * i - 100 * j <= 50 * c:
                ans += 1
    return str(ans)


if __name__ == '__main__':
    n = 4
    print(solve('\n'.join([input() for _ in range(n)])))
