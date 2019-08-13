def solve(string):
    a, b = map(int, string.split())
    return str(max(a + b, a - b, a * b))


if __name__ == '__main__':
    print(solve(input()))
