def solve(string):
    n, q, s, *lr = string.split()
    n = int(n)
    c = [0] * n
    count = 0
    for i in range(n):
        if i == 0:
            continue
        if s[i - 1:i + 1] == "AC":
            count += 1
        c[i] = count

    lr = list(map(int, lr))
    return "\n".join([str(c[r - 1] - c[l - 1]) for l, r in zip(lr[::2], lr[1::2])])


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve('{} {}\n'.format(n, m) + '\n'.join([input() for _ in range(m + 1)])))
