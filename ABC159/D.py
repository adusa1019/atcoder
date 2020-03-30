from collections import Counter


def solve(string):
    n, *a = map(int, string.split())
    c = Counter(a)
    b = sum(v * (v - 1) // 2 for v in c.values())
    return "\n".join(str(b - c[_a] + 1) for _a in a)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
