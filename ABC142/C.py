def solve(string):
    n, *a = map(int, string.split())
    ans = [0] * n
    for i, _a in enumerate(a, 1):
        ans[_a - 1] = str(i)
    return " ".join(ans)


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
