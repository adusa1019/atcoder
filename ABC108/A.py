def solve(string):
    k = int(string)
    return str((k // 2) * ((k + 1) // 2))


if __name__ == '__main__':
    print(solve(input()))
