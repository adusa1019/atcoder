from itertools import product


def solve(string):
    h, w, *s = string.split()
    h, w = int(h), int(w)
    s = ["#" * (w + 2)] + ["#" + _s + "#" for _s in s] + ["#" * (w + 2)]
    ans = 0
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def n(q, cx, cy):
        for x, y in d:
            nx = cx + x
            ny = cy + y
            if s[nx][ny] == ".":
                q.append((nx, ny, cx, cy))

    for _h, _w in product(range(1, h + 1), range(1, w + 1)):
        if s[_h][_w] == "#":
            continue
        q = list()
        n(q, _h, _w)
        if len(q) > 2:
            continue
        c = [[h * w] * (w + 2) for _ in range(h + 2)]
        c[_h][_w] = 0
        while q:
            cx, cy, px, py = q.pop()
            if c[px][py] + 1 >= c[cx][cy]:
                continue
            c[cx][cy] = c[px][py] + 1
            n(q, cx, cy)
        for i, j in product(range(1, h + 1), range(1, w + 1)):
            ans = max(ans, c[i][j] * (s[i][j] == "."))
    return str(ans)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
