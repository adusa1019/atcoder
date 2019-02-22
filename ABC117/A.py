def solve(string):
    t, x = map(int, string.split())
    return t / x


if __name__ == '__main__':
    print(solve(input()))
