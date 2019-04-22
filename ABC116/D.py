def solve(string):
    n, k, *td = map(int, string.split())
    td = sorted([(t, d) for t, d in zip(td[::2], td[1::2])], key=lambda x: x[1], reverse=True)
    max_variety = len(set([c[0] for c in td]))
    choice = td[:k]
    r, v, b = [], set([]), 0
    for _c in choice:
        b += _c[1]
        if _c[0] in v:
            r.append(_c[1])
        else:
            v.add(_c[0])
    b += len(v)**2
    i = k
    ans = [b]
    while len(v) < min(max_variety, k):
        while td[i][0] in v:
            i += 1
        v.add(td[i][0])
        ans.append(ans[-1] - r.pop() + td[i][1] + 2 * len(v) - 1)
    return str(max(ans))


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve('{} {}\n'.format(n, m) + '\n'.join([input() for _ in range(n)])))
