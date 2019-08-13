from collections import Counter


def solve(string):
    n, *ss = string.split()
    d = Counter("".join(sorted(s)) for s in ss)
    return str(sum([v * (v - 1) // 2 for v in d.values()]))


if __name__ == '__main__':
    n = int(input())
    print(solve('{}\n'.format(n) + '\n'.join([input() for _ in range(n)])))
