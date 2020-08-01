def solve(string):
    return str((1000 - (int(string) % 1000)) % 1000)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
