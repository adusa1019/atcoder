def solve(string):
    a, b = map(int, string.split())
    return str(max(0, a - 2 * b))


if __name__ == '__main__':
    print(solve(input()))
