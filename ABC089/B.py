def solve(string):
    n, *s = string.split()
    return "Three" if len(set(s)) == 3 else "Four"


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
