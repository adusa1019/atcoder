def solve(string):
    n, m, *a = map(int, string.split())
    while m > 0:
        a.sort(reverse=True)
        if a[0] == 0:
            break
        b = a[0] // 2
        for i, _a in enumerate(a):
            if m == 0 or _a <= b:
                break
            a[i] //= 2
            m -= 1
    return str(sum(a))


if __name__ == '__main__':
    print(solve('\n'.join([input(), input()])))
