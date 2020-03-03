def solve(string):
    n, k = map(int, string.split())
    c = 1
    while n >= k:
        c += 1
        n //= k
    return str(c)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
