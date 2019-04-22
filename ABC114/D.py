def solve(string):
    n = int(string)
    d = [0] * (n + 1)
    for i in range(2, n + 1):
        t = i
        for j in range(2, i + 1):
            while t % j == 0:
                d[j] += 1
                t //= j

    def f(n):
        return len(list(filter(lambda x: x >= n - 1, d)))

    f3, f5 = f(3), f(5)
    return str(f(75) + f(25) * (f3 - 1) + f(15) * (f5 - 1) + f5 * (f5 - 1) // 2 * (f3 - 2))


if __name__ == '__main__':
    print(solve(input()))
