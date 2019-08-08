def solve(string):
    a, b = map(int, string.split())
    return str(abs(a + b) // 2) if ((a + b) / 2).is_integer() else "IMPOSSIBLE"


if __name__ == '__main__':
    print(solve(input()))
