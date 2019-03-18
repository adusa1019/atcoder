def solve(string):
    a, b, c = map(int, string.split())
    return str(min(c, b // a))


if __name__ == '__main__':
    print(solve(input()))
