from itertools import accumulate


def solve(string):
    n, w, *stp = map(int, string.split())
    _sum = [0] * (2 * 10**5 + 1)
    for s, t, p in zip(*[iter(stp)] * 3):
        _sum[s] += p
        _sum[t] -= p
    return "Yes" if max(accumulate(_sum)) <= w else "No"


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
