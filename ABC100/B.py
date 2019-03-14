def solve(string):
    d, n = map(int, string.split())
    return str(100**d * n) if n < 100 else str(100**d * (n + 1))


if __name__ == '__main__':
    print(solve(input()))
