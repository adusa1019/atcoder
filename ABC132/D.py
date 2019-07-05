from scipy.special import comb


def solve(string):
    n, k = map(int, string.split())
    ans = []
    for i in range(1, k + 1):
        base = comb(n - k + 1, i, exact=True)
        var = comb(k - 1, i - 1, exact=True)
        ans.append(str(base * var % (10**9 + 7)))
    return "\n".join(ans)


if __name__ == '__main__':
    print(solve(input()))
