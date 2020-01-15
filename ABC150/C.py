from itertools import permutations


def solve(string):
    n, *pq = map(int, string.split())
    *ps, = permutations(range(1, n + 1))
    return str(abs(ps.index(tuple(pq[n:])) - ps.index(tuple(pq[:n]))))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
