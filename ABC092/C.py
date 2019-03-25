def solve(string):
    n, *a = map(int, string.split())
    a = [0] + a + [0]
    diff = [abs(j - i) for i, j in zip(a, a[1:])]
    base = sum(diff)
    ans = [str(base - diff[i] - diff[i + 1] + abs(a[i + 2] - a[i])) for i in range(n)]
    return "\n".join(ans)


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
