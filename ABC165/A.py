def solve(string):
    k, a, b = map(int, string.split())
    return "OK" if b - a >= k or min(map(lambda x: x % k, range(a, b + 1))) == 0 else "NG"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
