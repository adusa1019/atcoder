def solve(string):
    a, b = map(int, string.split())
    return str(a * b if 1 <= a <= 9 and 1 <= b <= 9 else -1)


if __name__ == '__main__':
    print(solve(input()))
