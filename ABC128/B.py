def solve(string):
    n, *sp = string.split()
    sp = sorted([(s, -int(p), i) for i, (s, p) in enumerate(zip(*[iter(sp)] * 2), start=1)])
    return "\n".join([str(i) for *_, i in sp])


if __name__ == '__main__':
    n = int(input())
    print(solve('{}\n'.format(n) + '\n'.join([input() for _ in range(n)])))
