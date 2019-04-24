def solve(string):
    n = int(string)
    dp = [[0] * 4 for _ in range(n)]
    dp[0] = [1] * 4
    for i in range(1, n):
        base = sum(dp[i - 1])
        for j in range(4):
            dp[i][j] = base
        # "AGC", "ACG", "GAC"
        if i >= 2:
            dp[i][1] -= dp[i - 2][0] + dp[i - 2][2]
            dp[i][2] -= dp[i - 2][0]
        # "AG{}C", "A{}GC"
        if i >= 3:
            dp[i][1] -= dp[i - 3][0] * 3
            dp[i][2] += dp[i - 3][2]

    return str(sum(dp[n - 1]) % (10**9 + 7))


if __name__ == '__main__':
    print(solve(input()))
