def solve(string):
    n, *uvw = map(int, string.split())
    g = [[] for _ in range(n + 1)]
    for u, v, w in zip(uvw[::3], uvw[1::3], uvw[2::3]):
        g[u].append((v, w))
        g[v].append((u, w))
    s = [(1, 0)]
    w = [-1] * (n + 1)
    while s:
        _s, _w = s.pop()
        w[_s] = _w % 2
        for _t, _w_ in g[_s]:
            if w[_t] == -1:
                s.append((_t, _w + _w_))
    return "\n".join(str(_w) for _w in w[1:])


if __name__ == '__main__':
    n = int(input())
    print(solve('{}\n'.format(n) + '\n'.join([input() for _ in range(n - 1)])))
