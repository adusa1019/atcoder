def solve(string):
    n, m, *abc = map(int, string.split())
    a = sorted(abc[:n])
    cb = sorted(list(zip(*[iter(abc[n:][::-1])] * 2)))
    i = ans = 0
    for c, b in cb[::-1]:
        start = i
        while i < n and a[i] < c and b > 0:
            i += 1
            b -= 1
            ans += c
        if start == i:
            break
    ans += sum(a[i:]) if i < n else 0
    return str(ans)


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve('{} {}\n'.format(n, m) + '\n'.join([input() for _ in range(m + 1)])))
