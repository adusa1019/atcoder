from collections import deque


def solve(string):
    n, *ab = map(int, string.split())
    e = [[] for _ in range(n + 1)]
    q = deque([1])
    c = [0] * (n + 1)
    for a, b in zip(*[iter(ab)] * 2):
        e[a].append(b)
    while q:
        s = q.popleft()
        d = 0
        for t in e[s]:
            d += 1 + (d + 1 == c[s])
            c[t] = d
            q.append(t)
    return str("{}\n{}".format(max(c), "\n".join(str(c[b]) for _, b in zip(*[iter(ab)] * 2))))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
