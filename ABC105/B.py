def solve(string):
    n = int(string)
    return "Yes" if any([(n - 7 * i) % 4 == 0 for i in range(n // 7 + 1)]) else "No"


if __name__ == '__main__':
    print(solve(input()))
