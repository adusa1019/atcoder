def solve(string):
    a, p = map(int, string.split())
    return str((a * 3 + p) // 2)


if __name__ == '__main__':
    print(solve(input()))
