from itertools import accumulate


def solve(string):
    n, k, *v = map(int, string.split())
    ans = 0
    for i in range(k + 1):
        for j in range(k - i + 1):
            base = sorted(v[:i] + v[max(n - k + i + j, i):])
            ans = max(ans, sum([b for l, b in enumerate(base) if b >= 0 or j <= l]))
    return str(ans)


def solve(string):
    n, k, *v = map(int, string.split())
    r = min(n, k)
    """
    for i in range(k + 1):
        for j in range(k - i + 1):
            base = sorted(v[:i] + v[max(n - k + i + j, i):])
            ans = max(ans, sum([b for l, b in enumerate(base) if b >= 0 or j <= l]))
    """

    def s(w):
        l = [0] * (k + 1)
        for i in range(1, k + 1):
            _w = sorted(w[:i], reverse=True)
            tmp = sum(_w)
            l[i] = max(l[i], tmp)
            j = 0
            while i + j < k and _w and _w[-1] < 0:
                j += 1
                tmp -= _w.pop()
                l[i + j] = max(l[i + j], tmp)
        return accumulate(l, func=max)

    *lefts, = s(v)
    *rights, = s(v[::-1])
    ans = max([lefts[i] + rights[k - i] for i in range(k + 1)])
    ans = min(ans, sum([_v for _v in v if _v > 0]))
    return str(ans)


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
