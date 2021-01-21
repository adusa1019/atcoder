def solve(string):
    n, *x = map(lambda x: abs(int(x)), string.split())
    return "\n".join(map(str, [sum(x), sum(map(lambda a: a**2, x))**0.5, max(x)]))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
