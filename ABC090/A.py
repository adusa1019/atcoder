def solve(string):
    c = "".join(string.split())
    return c[0] + c[4] + c[-1]


if __name__ == '__main__':
    n = 3
    print(solve('\n'.join([input() for _ in range(n)])))
