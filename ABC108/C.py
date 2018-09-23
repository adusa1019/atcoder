def solve(string):
    n, k = map(int, string.split(" "))
    ans = 0
    if k % 2 == 1:
        ans = (n // k)**3
    else:
        ans = (n // k)**3 + ((n // k) + 1)**3 if n % k >= (k // 2) else 2 * ((n // k)**3)
    return str(ans)


if __name__ == '__main__':
    print(solve(input()))
