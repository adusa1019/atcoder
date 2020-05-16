def f(n):
    return n * (n + 1) // 2


def solve(string):
    n = int(string)
    return str(f(n) - 3 * f(n // 3) - 5 * f(n // 5) + 15 * f(n // 15))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
