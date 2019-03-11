def solve(string):
    a = sorted(map(int, string.split()))
    return str(sum([abs(a1 - a0) for a0, a1 in zip(a, a[1:])]))


if __name__ == '__main__':
    print(solve(input()))
