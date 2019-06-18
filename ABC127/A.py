def solve(string):
    a, b = map(int, string.split())
    return str(b) if a >= 13 else "0" if a <= 5 else str(b // 2)


if __name__ == '__main__':
    print(solve(input()))
