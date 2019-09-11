def solve(string):
    n, *a = map(int, string.split())
    ans = [sum(a) - 2 * sum(a[1::2])]
    for _a in a[:-1]:
        ans.append(2 * _a - ans[-1])
    return " ".join(map(str, ans))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
