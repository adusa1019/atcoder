def check(l):
    c0 = all(l[i] for i in range(0, 9, 3))
    c1 = all(l[i] for i in range(1, 9, 3))
    c2 = all(l[i] for i in range(2, 9, 3))
    r0 = all(l[i] for i in range(3))
    r1 = all(l[i] for i in range(3, 6))
    r2 = all(l[i] for i in range(6, 9))
    x0 = all(l[i] for i in [0, 4, 8])
    x1 = all(l[i] for i in [2, 4, 6])
    return c0 or c1 or c2 or r0 or r1 or r2 or x0 or x1


def solve(string):
    *anb, = map(int, string.split())
    a, _, b = anb[:9], anb[9], anb[10:]
    return "Yes" if check([_a in b for _a in a]) else "No"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
