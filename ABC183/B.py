def solve(string):
    sx, sy, gx, gy = map(int, string.split())
    return str(sx + sy * (gx - sx) / (gy + sy))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
