def solve(string):
    a, b, c, d = map(int, string.split())
    return "Yes" if abs(a - c) <= d or abs(a - b) <= d and abs(b - c) <= d else "No"


if __name__ == '__main__':
    print(solve(input()))
