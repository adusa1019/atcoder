def solve(string):
    a, b, s = string.split()
    a = int(a)
    return "Yes" if s[a] == "-" and (s[:a] + s[a + 1:]).isdigit() else "No"


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
