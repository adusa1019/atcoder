def solve(string):
    n, s = string.split()
    return str(max([len(set(s[:i]) & set(s[i:])) for i in range(1, int(n))]))


if __name__ == '__main__':
    print(solve("\n".join([input(), input()])))
