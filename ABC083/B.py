def solve(string):
    n, a, b = map(int, string.split())

    def check(i):
        return a <= sum([int(_i) for _i in str(i)]) <= b

    return str(sum([i for i in range(n + 1) if check(i)]))


if __name__ == '__main__':
    print(solve(input()))
