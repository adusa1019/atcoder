from math import ceil


def solve(string):
    a, b = map(int, string.split())
    ans = ceil(a / 0.08)
    while ans // 10 < b:
        ans += 1
    return str(ans) if ans * 2 // 25 == a and ans // 10 == b else "-1"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
