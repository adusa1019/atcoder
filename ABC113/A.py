def solve(string):
    x, y = map(int, string.split())
    return str(x + y // 2)


if __name__ == '__main__':
    print(solve(input()))
