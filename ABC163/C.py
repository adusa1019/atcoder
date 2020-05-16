def solve(string):
    n, *a = map(int, string.split())
    ans = [0] * n
    for _a in a:
        ans[_a - 1] += 1
    return "\n".join(map(str, ans))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
