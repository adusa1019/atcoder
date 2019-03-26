def solve(string):
    n, m = map(int, string.split())
    if n == 1 and m == 1:
        return "1"
    elif n == 1 or m == 1:
        return str(max(n - 2, m - 2))
    elif n == 2 or m == 2:
        return "0"
    else:
        return str((n - 2) * (m - 2))


if __name__ == '__main__':
    print(solve(input()))
