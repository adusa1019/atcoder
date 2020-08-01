from collections import Counter


def solve(string):
    n, *s = string.split()
    c = Counter(s)
    return "\n".join(f"{k} x {c[k]}" for k in "AC WA TLE RE".split())


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
