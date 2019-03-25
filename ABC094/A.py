def solve(string):
    a, b, x = map(int, string.split())
    return "YES" if 0 <= (x - a) <= b else "NO"


if __name__ == '__main__':
    print(solve(input()))
