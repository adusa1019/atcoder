def solve(string):
    a, b = map(int, string.split())
    return "Even" if a * b % 2 == 0 else "Odd"


if __name__ == '__main__':
    print(solve(input()))
