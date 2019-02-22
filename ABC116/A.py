def solve(string):
    l = sorted(map(int, string.split()))
    return str(l[0] * l[1] // 2)


if __name__ == '__main__':
    print(solve(input()))
