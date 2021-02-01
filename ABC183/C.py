from itertools import permutations, chain


def solve(string):
    n, k, *t = map(int, string.split())

    return str(
        sum(
            sum(t[n * s + g]
                for s, g in zip(chain([0], p), chain(p, [0]))) == k
            for p in permutations(range(1, n))))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
