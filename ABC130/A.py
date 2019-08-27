def solve(string):
    x, a = map(int, string.split())
    return "0" if x < a else "10"


if __name__ == '__main__':
    print(solve(input()))
