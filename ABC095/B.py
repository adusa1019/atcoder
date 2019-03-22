def solve(string):
    n, x, *m = map(int, string.split())
    return str(n + (x - sum(m)) // min(m))


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve('{} {}\n'.format(n, m) + '\n'.join([input() for _ in range(n)])))
