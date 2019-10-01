def solve(string):
    n = int(string)
    return str((n+1) // 2 / n)


if __name__ == '__main__':
    print(solve(input()))
