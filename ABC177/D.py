class UF:

    def __init__(self, n):
        self.t = [-1] * (n + 1)

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if ra > rb:
            ra, rb = rb, ra
        self.t[ra], self.t[rb] = self.t[ra] + self.t[rb], ra

    def find(self, x):
        t = []
        while self.t[x] > 0:
            t.append(x)
            x = self.t[x]
        for _t in t:
            self.t[_t] = x
        return x


def solve(string):
    n, m, *ab = map(int, string.split())
    uf = UF(n)
    for a, b in zip(*[iter(ab)] * 2):
        uf.union(a, b)
    return str(-min(uf.t))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
