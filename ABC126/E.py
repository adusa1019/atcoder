def solve(string):
    n, m, *xyz = map(int, string.split())
    t = [-1] * (n + 1)

    def union(r1, r2):
        if r1 != r2:
            t[max(r1, r2)] = min(r1, r2)

    def find(x):
        if t[x] < 0:
            return x
        t[x] = find(t[x])
        return t[x]

    for x, y, _ in zip(*[iter(xyz)] * 3):
        union(find(x), find(y))
    return str(t.count(-1) - 1)


def scipy_solve(string):
    from scipy.sparse import csr_matrix as csr
    from scipy.sparse.csgraph import connected_components as cc
    n, m, *xyz = map(int, string.split())
    return str(cc(csr(([1] * m, (xyz[::3], xyz[1::3])), shape=(n + 1, n + 1)))[0] - 1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve('{} {}\n'.format(n, m) + '\n'.join([input() for _ in range(m)])))
