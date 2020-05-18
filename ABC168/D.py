def solve(string):
    from collections import deque
    n, m, *ab = map(int, string.split())
    p = [[] for _ in range(n)]
    for a, b in zip(*[iter(ab)] * 2):
        p[a - 1].append(b - 1)
        p[b - 1].append(a - 1)
    s, ans, d = deque([0]), [0] * n, [0] + [n] * (n - 1)
    while s:
        c = s.popleft()
        for t in p[c]:
            if d[c] + 1 < d[t]:
                d[t] = d[c] + 1
                ans[t] = c + 1
                s.append(t)
    return "Yes\n" + "\n".join(map(str, ans[1:]))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
