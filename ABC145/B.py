def solve(string):
    n, s = string.split()
    n = int(n)
    return "Yes" if s[:n // 2] == s[n // 2:] else "No"


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
