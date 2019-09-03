def solve(string):
    n = int(string)
    return str(n * (n - 1) // 2)


if __name__ == '__main__':
    print(solve(input()))
