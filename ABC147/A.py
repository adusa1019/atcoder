def solve(string):
    *a, = map(int, string.split())
    return "win" if sum(a) <= 21 else "bust"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
