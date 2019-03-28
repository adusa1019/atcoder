import numpy as np


def solve(string):
    num_max = 100000
    primes = np.asarray([True for _ in range(num_max + 1)])
    primes[:2] = False
    for i in range(2, num_max + 1):
        if primes[i]:
            primes[i * 2::i] = False
    primes = set(np.arange(num_max + 1)[primes])
    like2017 = [1 if i in primes and (i + 1) // 2 in primes else 0 for i in range(num_max + 1)]
    cumsum = np.cumsum(like2017)

    q, *lr = map(int, string.split())
    return "\n".join([str(cumsum[r] - cumsum[l - 1]) for l, r in zip(lr[::2], lr[1::2])])


if __name__ == '__main__':
    n = int(input())
    print(solve('{}\n'.format(n) + '\n'.join([input() for _ in range(n)])))
