from collections import Counter


def solve(string):
    n, *rest = string.split()
    n = int(n)
    count = Counter(rest[:n])
    m = rest[n]
    count -= Counter(rest[n + 1:])
    return str(max(max(count.values()), 0)) if len(count) > 0 else "0"


if __name__ == '__main__':
    n = int(input())
    ins = '{}\n'.format(n) + '\n'.join([input() for _ in range(n)])
    m = int(input())
    print(solve(ins + '\n{}\n'.format(m) + '\n'.join([input() for _ in range(m)])))
