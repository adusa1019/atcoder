from itertools import accumulate


def solve(string):
    n, k, *a = map(int, string.split())
    *a, = accumulate([0] + a)
    s = e = 0
    ans = 0
    while e < n + 1:
        if a[e] - a[s] < k:
            e += 1
            continue
        ans += n - e + 1
        s += 1
    return str(ans)


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
