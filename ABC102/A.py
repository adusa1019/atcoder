def solve(string):
    n = int(string)
    return str(n) if n % 2 == 0 else str(2 * n)


if __name__ == '__main__':
    print(solve(input()))
