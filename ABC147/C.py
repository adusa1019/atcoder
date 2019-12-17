def solve(string):
    n, *axy = map(int, string.split())
    i = 0
    h = [set() for _ in range(n)]
    u = [set() for _ in range(n)]
    for j in range(n):
        a = axy[i]
        for x, y in zip(*[iter(axy[i + 1:i + 2 * a + 1])] * 2):
            if y == 1:
                h[j].add(x - 1)
            else:
                u[j].add(x - 1)
        i += 2 * a + 1

    def search(checking, honest, unkind):
        if len(honest & unkind) > 0:
            return 0
        if len(checking) == 0:
            return len(honest)
        t = checking.copy()
        c = t.pop()
        return max(search(t, honest | {c} | h[c], unkind | u[c]), search(t, honest, unkind | {c}))

    return str(search(set(range(n)), set(), set()))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
