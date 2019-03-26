from functools import reduce
from itertools import combinations
from operator import mul


def solve(string):
    n, *s = string.split()
    num = [len([True for _s in s if _s[0] == _i]) for _i in "M A R C H".split()]
    return str(sum([reduce(mul, n) for n in combinations(num[:5], 3)]))


if __name__ == '__main__':
    n = int(input())
    print(solve('{}\n'.format(n) + '\n'.join([input() for _ in range(n)])))
