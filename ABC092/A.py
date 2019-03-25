def solve(string):
    a, b, c, d = map(int, string.split())
    return str(min(a, b) + min(c, d))


if __name__ == '__main__':
    n = 4
    print(solve('\n'.join([input() for _ in range(n)])))
