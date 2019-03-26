def solve(string):
    n, a = map(int, string.split())
    return "Yes" if n % 500 <= a else "No"


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
