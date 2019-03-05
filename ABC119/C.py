from itertools import product


def solve(string):
    n, a, b, c, *l = map(int, string.split())
    ans = 3000
    for p in product(range(4), repeat=n):
        if not ({0, 1, 2} <= set(p)):
            continue
        sums = [0, 0, 0, 0]
        for _p, _l in zip(p, l):
            sums[_p] += _l
        mp12 = sum(abs(_s - _abc) for _s, _abc in zip(sums, [a, b, c]))
        mp3 = sum(1 for _p in p if _p < 3) - 3
        ans = min(ans, mp12 + mp3 * 10)
    return str(ans)


if __name__ == '__main__':
    n, a, b, c = map(int, input().split())
    print(solve('{} {} {} {}\n'.format(n, a, b, c) + '\n'.join([input() for _ in range(n)])))
