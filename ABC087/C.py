def solve(string):
    n, *a = map(int, string.split())
    return str(max([sum(a[:i+1]) + sum(a[-(n - i):]) for i in range(n)]))


if __name__ == '__main__':
    n = int(input())
    print(solve('{}\n'.format(n) + '\n'.join([input() for _ in range(2)])))
