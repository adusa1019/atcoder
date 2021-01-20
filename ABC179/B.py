def solve(string):
    n, *d = map(int, string.split())
    z = [d1 == d2 for d1, d2 in zip(*[iter(d)] * 2)]
    return "Yes" if any(z1 and z2 and z3 for z1, z2, z3 in zip(z, z[1:], z[2:])) else "No"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
