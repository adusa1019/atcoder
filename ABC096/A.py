def solve(string):
    a, b = map(int, string.split())
    return str(a) if a <= b else str(a - 1)


if __name__ == '__main__':
    print(solve(input()))
