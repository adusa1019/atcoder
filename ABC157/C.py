def solve(string):
    n, m, *sc = map(int, string.split())
    v = [0] * n
    for s, c in zip(*[iter(sc)] * 2):
        if (v[s - 1] > 0 and v[s - 1] != c) or (n > 1 and s == 1 and c == 0):
            return "-1"
        v[s - 1] = c
    if n > 1 and v[0] == 0:
        v[0] += 1
    return "".join(map(str, v))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
