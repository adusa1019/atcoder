def solve(string):
    s, t = string.split()
    return "Yes" if any([s[i:] + s[:i] == t for i in range(len(s))]) else "No"


if __name__ == '__main__':
    print(solve("\n".join([input(), input()])))
