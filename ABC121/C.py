def solve(string):
    n, m, *ab = map(int, string.split())
    ab = sorted([(a, b) for a, b in zip(ab[::2], ab[1::2])], key=lambda x: x[0])
    ans = 0
    for a, b in ab:
        if m <= b:
            ans += a * m
            break
        ans += a * b
        m -= b
    return str(ans)


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve('{} {}\n'.format(n, m) + '\n'.join([input() for _ in range(n)])))
