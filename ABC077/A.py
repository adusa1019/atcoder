def solve(string):
    c = string.split()
    return "YES" if c[0] == c[1][::-1] else "NO"


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
