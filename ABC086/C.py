def solve(string):

    n, *txy = map(int, string.split())
    checks = [
        abs(x) + abs(y) <= t and (t + x + y) % 2 == 0
        for t, x, y in zip(txy[::3], txy[1::3], txy[2::3])
    ]
    return "Yes" if all(checks) else "No"


if __name__ == '__main__':
    n = int(input())
    print(solve('{}\n'.format(n) + '\n'.join([input() for _ in range(n)])))
