from heapq import heappop, heappush
from collections import defaultdict


def solve(string):
    n, m, *ab = map(int, string.split())
    dd = defaultdict(list)
    for a, b in zip(*[iter(ab)] * 2):
        dd[a].append(-b)
    hq, ans = [], 0
    for d in range(1, m + 1):
        if d in dd:
            for _b in dd[d]:
                heappush(hq, _b)
        if hq:
            ans += heappop(hq)
    return str(-ans)


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve('{} {}\n'.format(n, m) + '\n'.join([input() for _ in range(n)])))
