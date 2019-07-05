def solve(string):
    n, k, s = string.split()
    n, k = int(n), int(k) - 1
    return s[:k] + s[k].lower() + s[k + 1:]


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
