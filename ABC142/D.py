from fractions import gcd


def solve(string):
    a, b = map(int, string.split())
    g = gcd(a, b)
    ans = 1 if g % 2 else 2
    while g % 2 == 0:
        g //= 2
    for i in range(3, int(g**0.5) + 1, 2):
        if g % i == 0:
            ans += 1
        while g % i == 0:
            g //= i
    return str(ans + 1) if g > 1 else str(ans)


if __name__ == '__main__':
    print(solve(input()))
