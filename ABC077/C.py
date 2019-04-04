def solve(string):
    n, *abc = map(int, string.split())
    a, b, c = map(sorted, [abc[i*n:(i+1)*n] for i in range(3)])
    ai = ci = ans = 0
    for _b in b:
        while ai < n and a[ai] < _b:
            ai += 1
        while ci < n and c[ci] <= _b:
            ci += 1
        ans += ai * (n - ci)
    return str(ans)


if __name__ == '__main__':
    n = int(input())
    print(solve('{}\n'.format(n) + '\n'.join([input() for _ in range(3)])))
