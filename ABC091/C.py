def solve(string):
    n, *abcd = map(int, string.split())
    abcd = [(ac, bd) for ac, bd in zip(abcd[::2], abcd[1::2])]
    ab = abcd[:n]

    candidate = []
    ans = 0
    ps = sorted(abcd, key=lambda x: x[0])
    for p in ps:
        if p in ab:
            candidate.append(p)
            candidate = sorted(candidate, key=lambda x: x[1], reverse=True)
        else:
            for i, _p in enumerate(candidate):
                if _p[1] < p[1]:
                    ans += 1
                    candidate.pop(i)
                    break
    return str(ans)


if __name__ == '__main__':
    n = int(input())
    print(solve('{}\n'.format(n) + '\n'.join([input() for _ in range(2 * n)])))
