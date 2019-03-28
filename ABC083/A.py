def solve(string):
    a, b, c, d = map(int, string.split())
    return "Left" if a + b > c + d else "Right" if a + b < c + d else "Balanced"


if __name__ == '__main__':
    print(solve(input()))
