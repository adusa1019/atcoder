def solve(string):
    n, d, x, *a = map(int, string.split())
    return str(sum([d // _a + 1 if d % _a > 0 else d // _a for _a in a]) + x)


if __name__ == '__main__':
    n = int(input())
    print(solve('{}\n'.format(n) + '\n'.join([input() for _ in range(n + 1)])))
