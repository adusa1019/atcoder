def solve(string):
    n, k, q, *a = map(int, string.split())
    t, b = [0] * n, q - k
    for _a in a:
        t[_a - 1] += 1
    return "\n".join(["Yes" if _t > b else "No" for _t in t])


if __name__ == '__main__':
    n, m, q = map(int, input().split())
    print(solve('{} {} {}\n'.format(n, m, q) + '\n'.join([input() for _ in range(q)])))
