def solve(string):
    s, t = string.split()
    return "Yes" if sorted(s) < sorted(t,reverse=True) else "No"


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
