def solve(string):
    from itertools import combinations_with_replacement
    n, m, q, *abcd = map(int, string.split())
    ans = 0
    for v in combinations_with_replacement(range(1, m + 1), n):
        ans = max(
            ans,
            sum(d if v[b - 1] - v[a - 1] == c else 0 for a, b, c, d in zip(*[iter(abcd)] * 4)))
    return str(ans)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
