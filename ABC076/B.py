def solve(string):
    n, k = map(int, string.split())
    tmp = 1
    while tmp < k and n > 0:
        tmp <<= 1
        n -= 1
    return str(tmp + n * k)


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
