def solve(string):
    n, *ab = map(int, string.split())
    return str(sum([(b + a) * (b - a + 1) for a, b in zip(*[iter(ab)] * 2)]) // 2)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
