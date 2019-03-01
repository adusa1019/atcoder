def solve(string):
    a = sorted(map(int, string.split()))
    return str(a[-1] * 10 + a[1] + a[0])


if __name__ == '__main__':
    print(solve(input()))
