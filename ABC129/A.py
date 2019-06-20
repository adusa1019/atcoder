def solve(string):
    *pqr, = map(int, string.split())
    return str(sum(sorted((pqr))[:2]))


if __name__ == '__main__':
    print(solve(input()))
