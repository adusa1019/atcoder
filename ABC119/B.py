def solve(string):
    n, *xu = string.split()
    return str(sum([int(x) if u == "JPY" else float(x) * 380000 for x, u in zip(xu[::2], xu[1::2])]))


if __name__ == '__main__':
    n = int(input())
    print(solve('{}\n'.format(n) + '\n'.join([input() for _ in range(n)])))
