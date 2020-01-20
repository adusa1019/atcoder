def solve(string):
    n, m, *ps = string.split()
    n = int(n)
    ac = [0] * n
    wa = [0] * n
    for p, s in zip(*[iter(ps)] * 2):
        p = int(p) - 1
        if s == "AC":
            ac[p] = 1
        elif not ac[p]:
            wa[p] += 1
    return "{} {}".format(sum(ac), sum([w * a for a, w in zip(ac, wa)]))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
