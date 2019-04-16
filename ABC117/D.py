def solve(string):
    n, k, *a = map(int, string.split())
    x = 0
    p = 2**(len("{:b}".format(k)) - 1)
    while p > 0:
        if sum([1 for _a in a if p & _a]) < n / 2 and x + p <= k:
            x += p
        p //= 2
    return str(sum([x ^ _a for _a in a]))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
