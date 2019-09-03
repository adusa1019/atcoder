def solve(string):
    a, b = map(int, string.split())
    return str((b - 2) // (a - 1) + 1)


if __name__ == '__main__':
    print(solve(input()))
