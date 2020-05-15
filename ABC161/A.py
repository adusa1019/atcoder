def solve(string):
    x, y, z = map(int, string.split())
    return f"{z} {x} {y}"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
