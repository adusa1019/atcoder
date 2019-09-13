def solve(string):
    n, *a = map(int, string.split())
    for i in range(n // 2, 0, -1):
        a[i - 1] = sum(a[i - 1::i]) % 2
    ans = [str(i + 1) for i, _a in enumerate(a) if _a == 1]
    return "0" if len(ans) == 0 else "{}\n{}".format(len(ans), " ".join(ans))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
