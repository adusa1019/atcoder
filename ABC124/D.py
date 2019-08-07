def solve(string):
    n, k, s = string.split()
    n, k = map(int, [n, k])
    flip = [0] + [i for i, (s0, s1) in enumerate(zip(s, s[1:]), start=1) if s0 != s1] + [n]
    start = int(s[0])
    l = len(flip) - 1
    return str(max([flip[min(l, i + 2 * k + (i % 2 ^ start))] - flip[i] for i in range(l + 1)]))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
