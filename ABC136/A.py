def solve(string):
    a, b, c = map(int, string.split())
    return str(max(c - a + b, 0))


if __name__ == '__main__':
    print(solve(input()))
