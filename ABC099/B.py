def solve(string):
    a, b = map(int, string.split())
    n = b - a
    return str(n * (n + 1) // 2 - b)


if __name__ == '__main__':
    print(solve(input()))
