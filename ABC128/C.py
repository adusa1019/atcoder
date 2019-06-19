from itertools import product


def solve(string):
    n, m, *ksp = map(int, string.split())
    p = ksp[-m:]
    ans = 0
    for t in product([True, False], repeat=n):
        index = 0
        for i, _p in enumerate(p):
            k = ksp[index]
            use = ksp[index + 1:index + 1 + k]
            index += k + 1
            if sum([t[j - 1] for j in use]) % 2 != _p:
                break
        else:
            ans += 1
    return str(ans)


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve('{} {}\n'.format(n, m) + '\n'.join([input() for _ in range(m + 1)])))
