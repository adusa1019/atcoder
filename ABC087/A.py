def solve(string):
    x, a, b = map(int, string.split())
    return str((x - a) % b)


if __name__ == '__main__':
    n = 3
    print(solve('\n'.join([input() for _ in range(n)])))
