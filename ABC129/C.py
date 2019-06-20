def solve(string):
    n, m, *a = map(int, string.split())
    ans = [0] * (n + 1)
    a = set(a)
    ans[0] = 1
    ans[1] = 0 if 1 in a else 1
    for i in range(2, n + 1):
        if i in a:
            continue
        ans[i] = (ans[i - 2] + ans[i - 1]) % 1000000007
    return str(ans[-1])


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve('{} {}\n'.format(n, m) + '\n'.join([input() for _ in range(m)])))
