from itertools import accumulate


def solve(string):
    n, m, q, *lrpq = map(int, string.split())
    lr, pq = lrpq[:2 * m], lrpq[2 * m:]
    t = [[0] * (n + 1) for _ in range(n + 1)]
    for l, r in zip(lr[::2], lr[1::2]):
        t[l][r] += 1
    t = [list(accumulate(t_)) for t_ in zip(*(accumulate(_t) for _t in t))]
    ans = [
        str(t[q][q] - t[p - 1][q] - t[q][p - 1] + t[p - 1][p - 1])
        for p, q in zip(pq[::2], pq[1::2])
    ]
    return "\n".join(ans)


if __name__ == '__main__':
    n, m, q = map(int, input().split())
    print(solve('{} {} {}\n'.format(n, m, q) + '\n'.join([input() for _ in range(m + q)])))
