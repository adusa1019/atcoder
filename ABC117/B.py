def solve(string):
    n, *l = map(int, string.split())
    l = sorted(l)
    return "Yes" if sum(l[:-1]) > l[-1] else "No"


if __name__ == '__main__':
    print(solve("\n".join([input(), input()])))
