def solve(string):
    n, q, *abpx = map(int, string.split())
    t, c, d, check = [[] for i in range(n + 1)], [0] * (n + 1), [1], [True] * (n + 1)
    for a, b in zip(*[iter(abpx[:2 * n - 2])] * 2):
        t[a].append(b)
        t[b].append(a)
    for p, x in zip(*[iter(abpx[2 * n - 2:])] * 2):
        c[p] += x
    while len(d) > 0:
        curr = d.pop()
        check[curr] = False
        next_ = [i for i in t[curr] if check[i]]
        for n_ in next_:
            c[n_] += c[curr]
        d.extend(next_)
    return " ".join([str(_c) for _c in c[1:]])


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve('{} {}\n'.format(n, m) + '\n'.join([input() for _ in range(n + m - 1)])))
