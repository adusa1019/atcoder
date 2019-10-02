def solve(string):
    a, b, m = 0, 1, 10**9 + 7
    for l in string:
        a, b = ((3 * a + b) % m, 2 * b % m) if l == "1" else (3 * a % m, b)
    return str((a + b) % m)


if __name__ == '__main__':
    print(solve(input()))
