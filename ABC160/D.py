def solve(string):
    n, x, y = map(int, string.split())
    ans = [0] * n
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            ans[min(j - i, abs(x - i) + 1 + abs(j - y), abs(y - i) + 1 + abs(j - x))] += 1
    return "\n".join(map(str, ans[1:]))


def fast_solve(string):
    n, x, y = map(int, string.split())
    ans = [n]
    a, b, c = x, y - x - 1, n - y + 1
    for i in range(2, n):
        pass
    return "\n".join(map(str, ans))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
