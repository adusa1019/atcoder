from fractions import gcd


def solve(string):
    a, b = map(int, string.split())
    return str(a * b // gcd(a, b))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
