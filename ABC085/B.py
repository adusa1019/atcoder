def solve(string):
    n, *d = map(int, string.split())
    return str(len(set(d)))


if __name__ == '__main__':
    n = int(input())
    print(solve('{}\n'.format(n) + '\n'.join([input() for _ in range(n)])))
