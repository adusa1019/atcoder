def solve(string):
    a, b = map(int, string.split())
    return str(max(2 * a - 1, a + b, 2 * b - 1))


if __name__ == '__main__':
    print(solve(input()))
