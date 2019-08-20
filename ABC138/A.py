def solve(string):
    a, s = string.split()
    return s if int(a) >= 3200 else "red"


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
