def solve(string):
    n = int(string)
    return str(sum((n - 1) // i for i in range(1, n)))


def fast_solve(string):
    n = int(string) - 1
    r = int(n**0.5)
    return str(2 * sum(n // i - i for i in range(1, r + 1)) + r)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
