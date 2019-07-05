def solve(string):
    n, k = map(int, string.split())
    ans = 0
    for i in range(1, n + 1):
        p = 1
        while i < k:
            i *= 2
            p /= 2
        ans += p

    return ans / n


if __name__ == '__main__':
    print(solve(input()))
