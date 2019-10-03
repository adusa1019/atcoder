from fractions import gcd


def solve(string):
    a, b, c, d = map(int, string.split())
    lcm = c * d // gcd(c, d)
    return str(b - a + 1 - (b // c - (a - 1) // c + b // d - (a - 1) // d - b // lcm +
                            (a - 1) // lcm))


if __name__ == '__main__':
    print(solve(input()))
